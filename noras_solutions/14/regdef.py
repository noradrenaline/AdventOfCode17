class register:
	def __init__(self,regsize):
		# keeping the whole array of addresses is a little silly
		# it would be better to just keep location of 0
		# TODO: change self.addresses to integer self.start
		#self.addresses = range(regsize)
		self.idx = 0
		self.regsize = regsize
		self.values = range(regsize)
		self.skipsize = 0
		self.lastlength = 0
	def advance(self):
		r = (self.skipsize + self.lastlength)%self.regsize
		self.skipsize += 1
		self.idx = (self.idx-r)%self.regsize
		self.values = self.values[r:]+self.values[:r]
	def swap(self,leng):
		if leng > self.regsize:
			print "invalid length encountered"
			exit()
		self.lastlength = leng
		self.values = self.values[:leng][::-1] + self.values[leng:]
	def rehome(self):
		i = self.idx
		self.values = self.values[i:] + self.values[:i]


def xorus(seq):
	res = 0
	for val in seq:
		res = res^val
	return res


def hashme(vec):	
	regsize = 256
	numreps = 64
	binsize = 16

	reg = register(regsize)
	#with open('input.txt') as fh:
	#	vec = fh.read().strip()
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

	condensed = [None]*(regsize/binsize)
	for bin in range(regsize/binsize):
		condensed[bin] = xorus(reg.values[bin*binsize:(bin+1)*binsize])

	# annnnnd get it into hex:
	answer = ''
	for val in condensed:
		answer = answer + format(val,'02x')

	return answer
	

	
