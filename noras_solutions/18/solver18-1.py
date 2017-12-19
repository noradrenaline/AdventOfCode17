# this feels ungraceful. Hm.
# you could build some evals instead, I guess.........
class regi:
	def __init__(self, cmdlist):
		self.registers = {}
		self.lastsound = 0
		self.cmdnum = 0
		self.cmdlist = cmdlist
		self.recovery = 0
		self.valueWasRecovered = 0
	def operate(self):
		words = self.cmdlist[self.cmdnum].split()
		jumplen = 1
		# initialize the register(s) involved:
		if words[1] not in self.registers:
			self.registers[words[1]] = 0
		# arg 1 is always a register. Need to handle arg 2:
		if len(words)==3:
			if words[2][-1].isdigit():
				arg2 = int(words[2])
			else:
				if words[2] not in self.registers:
					self.registers[words[2]] = 0
				arg2 = int(self.registers[words[2]])
			
		# okay, now we can execute the relevant commands
		if words[0] == 'snd':
			self.lastsound = self.registers[words[1]]
		elif words[0] == 'set':
			self.registers[words[1]] = arg2
		elif words[0] == 'add':
			self.registers[words[1]] += arg2
		elif words[0] == 'mul':
			self.registers[words[1]] *= arg2
		elif words[0] == 'mod':
			self.registers[words[1]] %= arg2
		elif words[0] == 'rcv':
			if self.registers[words[1]] != 0:
				self.recovery = self.lastsound
				self.valueWasRecovered += 1
		elif words[0] == 'jgz':
			if self.registers[words[1]] > 0:
				jumplen = arg2
		else:
			print "error error error"
			exit()
		self.cmdnum += jumplen
		

# yeesh.
	
with open("input.txt") as fh:
	cmdlist = fh.readlines()
myreg = regi(cmdlist)
itercount = 0
while myreg.valueWasRecovered == 0 and itercount < 1000000:
	myreg.operate()
	itercount+=1
print "the whole situation took " + str(itercount) + " operations."
print myreg.recovery

