source = "input.txt"

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

# get an array of scanners from the input
scanners = {}
maxdep = 0
with open(source) as fh:
	for line in fh:
		(dep,ran) = line.split(": ")
		scanners[int(dep)] = scanner(int(dep),int(ran))
		maxdep = max(int(dep),maxdep)

print "this firewall is " + str(maxdep) + " layers deep."

severity = 0
for i in range(maxdep+1):
	if i in scanners and scanners[i].position == 0:
		print "Caught in layer " + str(i)
		severity += i*scanners[i].ran
	[scanners[x].tick() for x in scanners]

print "The severity of the trip was " + str(severity)
