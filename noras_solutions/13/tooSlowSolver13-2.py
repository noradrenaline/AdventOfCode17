source = "fakeinput.txt"

class scanner:
	def __init__(self,dep,ran):
		self.dep = dep;
		self.ran = ran;
		self.position = 0 # I want to start at 1 but we python now boyz
		self.direction = 1
	def tick(self):
		if self.ran == 1:
			return
		elif self.position == 0:
			self.direction = 1
		elif self.position == self.ran-1:
			self.direction = -1
		self.position += self.direction
	def copy(self):
		c = scanner(self.dep,self.ran)
		c.position = self.position
		c.direction = self.position
		return c

# get an array of scanners from the input
startingScanners = {}
maxdep = 0
with open(source) as fh:
	for line in fh:
		(dep,ran) = line.split(": ")
		startingScanners[int(dep)] = scanner(int(dep),int(ran))
		maxdep = max(int(dep),maxdep)


def doIescape(delay,scanners,maxdep):
	severity = 0
	for _ in range(delay):
		[scanners[x].tick() for x in scanners]
	for i in range(maxdep+1):
		if i in scanners and scanners[i].position == 0:
			return 0
		[scanners[x].tick() for x in scanners]
	return 1


escaped = 0
delay = 0
while escaped == 0 and delay < 100000000:
	delay += 1
	# I swear to fuck just make a fucking copy of the thing I am fucking telling you to copy
	scanners = {}
	for x in startingScanners:
		scanners[x] = startingScanners[x].copy()
	escaped = doIescape(delay,scanners,maxdep)

print "You escape if you wait for a delay of " + str(delay) + " picoseconds."
