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
	def printstr(self):
		print ''.join(self.arrangement)

lu = lineup(lsize)

for cmd in moves:
	lu.dance(cmd)

lu.printstr()
	
