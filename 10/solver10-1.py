class register:
	def __init__(self,regsize):
		self.addresses = range(regsize)
		self.values = range(regsize)
		self.skipsize = 0
		self.lastlength = 0
	def advance(self):
		r = (self.skipsize + self.lastlength)%len(self.addresses)
		self.skipsize += 1
		self.addresses = self.addresses[r:]+self.addresses[:r]
		self.values = self.values[r:]+self.values[:r]
	def swap(self,leng):
		if leng > len(self.addresses):
			print "invalid length encountered"
			exit()
		self.lastlength = leng
		self.values = self.values[:leng][::-1] + self.values[leng:]
	def rehome(self):
		i = self.addresses.index(0)
		self.addresses = self.addresses[i:] + self.addresses[:i]
		self.values = self.values[i:] + self.values[:i]
	

# test it on the lilguy:
#myReg = register(5)
#input = [3,4,1,5]
#for r in input:
#	#myReg = myReg.swap(r).advance() # huh, can't stack 'em?
#	myReg.swap(r)
#	myReg.advance()
#myReg.rehome()
#print myReg.values

# okay now we just gotta handle the input.
reg = register(256)
with open('input.txt') as fh:
	vec = fh.read().split(",")
for v in vec:
	reg.swap(int(v))
	reg.advance()

# easier to rehome than to deal with the case where 0 is currently the last element:
reg.rehome()
answer = reg.values[0]*reg.values[1]
print "answer: " + str(answer)
	
