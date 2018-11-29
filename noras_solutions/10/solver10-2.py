class register:
	def __init__(self,regsize):
		# keeping the whole array of addresses is a little silly
		# it would be better to just keep location of 0
		# TODO: change self.addresses to integer self.start
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
	
regsize = 256
numreps = 64
binsize = 16

reg = register(regsize)
with open('input.txt') as fh:
	vec = fh.read().strip()
extrajunk = [17,31,73,47,23]

for repeat in range(numreps):
	for c in vec:
		v = ord(c)
		reg.swap(v)
		reg.advance()
	for e in extrajunk:
		reg.swap(e)
		reg.advance()

reg.rehome()

# now we have to deal with the output thing
def xorus(seq):
	res = 0
	for val in seq:
		res = res^val
	return res

condensed = [None]*(regsize/binsize)
for bin in range(regsize/binsize):
	condensed[bin] = xorus(reg.values[bin*binsize:(bin+1)*binsize])

# annnnnd get it into hex:
answer = ''
for val in condensed:
	answer = answer + format(val,'02x')

print answer
	
