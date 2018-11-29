lsize = 16
with open("input.txt") as fh:
	moves = fh.read().strip().split(',')

class lineup:
	def __init__(self,sz):
		s = 'abcdefghijklmnopqrstuvwxyz'[:sz]
		self.arrangement = list(s)
	def dance(self,cmd):
		if cmd[0] == 's':
			r = int(cmd[1:])
			self.arrangement = self.arrangement[-r:]+self.arrangement[:-r]
		elif cmd[0] == 'x':
			[p1,p2] = cmd[1:].split('/')
			t = self.arrangement[int(p1)]
			self.arrangement[int(p1)] = self.arrangement[int(p2)]
			self.arrangement[int(p2)] = t
		elif cmd[0] == 'p':
			[c1,c2] = cmd[1:].split('/')
			i1 = self.arrangement.index(c1)
			i2 = self.arrangement.index(c2)
			self.arrangement[i1] = c2
			self.arrangement[i2] = c1
		else:
			print 'unknown command encountered'
	def stringify(self):
		return ''.join(self.arrangement)

lu = lineup(lsize)
# a billion is too many apparently. Why the f is it ooming? 
# I was expecting it to be super-slow, but why oom? Isn't it true that
# the only thing in the memory is the one lineup and the input instructions?
# WTF gives?
# Maybe we can just map the beginning order to the end order
# and apply the same transformation to a different starting order--
# shit, no, that won't work because of the p operator which cares about
# letters, not positions.
# it is true that if we ever land on existing order, then it will
# continue to run the same loop. But there are 16! possible orderings, 
# which is way more than a billion, so will that ever happen.

# let me try to loop a shorter number of times and see if there is a closed loop, maybe?
# if there is then the solution is analytic up to the number of times you can do the loop in a billion reps

i = 0;
occurrence = {'abcdefghijklmnop':0}
while (i<1000):
	for cmd in moves:
		lu.dance(cmd)
	i+=1
	s = lu.stringify()
	if s not in occurrence:
		occurrence[s] = i
	else: 
		print "string " + s + " occurred at " + str(occurrence[s]) + " and also at " + str(i)
		break
if i == 1000:
	print "Your shit is fucked."
# okay, so we DID find a repeat! 
#firstocc = occurrence[s]
#secondocc = i
# so how many full loops fit below 1 billion?
# can I assume that only one starting string would possibly give rise to the loop one?
# well, in this case I know it is, because we do indeed loop back to abcdefghijklmnop
# I'm not convinced that this is a general condition (e.g. there couldn't be multiple routes into
# a single loop), but then, I'm also not convinced that the solution is general at all because it 
# could be the case that there wasn't a loop in a reasonable amount of time. Oh well.
# i is now the looplength.

numToRun = 1000000000 % i
# lu is currently in the desired state, alphabetically ordered, right?
print "sanity check:"
print lu.stringify()
print "now running the final " + str(numToRun) + "dances."
for _ in range(numToRun):
	for cmd in moves:
		lu.dance(cmd)

print "final layout:"
print lu.stringify()
	
