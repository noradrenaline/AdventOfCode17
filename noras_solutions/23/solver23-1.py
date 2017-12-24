class regi:
	def __init__(self,cmdlist):
		self.registers = {}
		self.cmdnum = 0
		self.cmdlist = cmdlist
		self.mulcount = 0
	def operate(self):
		words = self.cmdlist[self.cmdnum].split()
		jumplen = 1
		# the entire command dictionary for this problem expects two arguments
		# it's possible for both to be integers
		if words[1][-1].isdigit():
			arg1 = int(words[1])
		elif words[1] not in self.registers:
			self.registers[words[1]] = 0
			arg1 = 0
		else:
			arg1 = self.registers[words[1]]
		if words[2][-1].isdigit():
			arg2 = int(words[2])
		elif words[2] not in self.registers:
			self.registers[words[2]] = 0
			arg2 = 0
		else:
			arg2 = self.registers[words[2]]
		
		# now execute the command
		if words[0] == "set":
			self.registers[words[1]] = arg2
		elif words[0] == "sub":
			self.registers[words[1]] -= arg2
		elif words[0] == "mul":
			self.registers[words[1]] *= arg2
			self.mulcount+=1
		elif words[0] == "jnz":
			if arg1 != 0:
				jumplen = arg2
		else:
			print "error error error"
			exit()
		
		self.cmdnum += jumplen


# get that input then:
with open("input.txt") as fh:
	cmdlist = fh.readlines()

newreg = regi(cmdlist)
clistsize = len(cmdlist)
itercount = 0

while newreg.cmdnum >= 0 and newreg.cmdnum < clistsize and itercount < 1000000:
	newreg.operate()
	itercount += 1

print "In " + str(itercount) + " operations, we called multiply " + str(newreg.mulcount) + " times."



