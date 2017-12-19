from collections import deque

class regi:
	def __init__(self, cmdlist,p):
		self.registers = {"p":p}
		self.sendval = 0
		self.sendflag = 0
		self.cmdnum = 0
		self.cmdlist = cmdlist
		self.cmdlen = len(cmdlist)
		self.queue = deque()
		self.terminated = 0
		self.stalled = 0
	def operate(self):
		words = self.cmdlist[self.cmdnum].split()
		jumplen = 1
		self.sendflag = 0
		# initialize the register(s) involved:
		# oh shiiii, words[1] can be an int now
		# (in theory, and for the test. We know it isn't
		# in the actual input.)
		if words[1][-1].isdigit():
			arg1 = int(words[1]) # for use in send only - and jgz
		else:
			if words[1] not in self.registers:
				self.registers[words[1]] = 0
			arg1 = int(self.registers[words[1]])
		if len(words)==3:
			if words[2][-1].isdigit():
				arg2 = int(words[2])
			else:
				if words[2] not in self.registers:
					self.registers[words[2]] = 0
				arg2 = int(self.registers[words[2]])
			
		# okay, now we can execute the relevant commands
		if words[0] == 'snd':
			self.sendval = arg1
			self.sendflag = 1
		elif words[0] == 'set':
			self.registers[words[1]] = arg2
		elif words[0] == 'add':
			self.registers[words[1]] += arg2
		elif words[0] == 'mul':
			self.registers[words[1]] *= arg2
		elif words[0] == 'mod':
			self.registers[words[1]] %= arg2
		elif words[0] == 'rcv':
			#if self.registers[words[1]] != 0:
			if len(self.queue) > 0:
				self.registers[words[1]] = self.queue.popleft()
			else:
				self.stalled = 1	
				jumplen = 0 # don't move on
		elif words[0] == 'jgz':
			if arg1 > 0:
				jumplen = arg2
		else:
			print "error error error"
			exit()
		self.cmdnum += jumplen
		if self.cmdnum < 0 or self.cmdnum >= self.cmdlen:
			self.terminated = 1
	def addQueue(self,val):
		self.queue.append(val)
		self.stalled = 0

# yeesh.
def terminatedstate(r0,r1):
	# is this the right terminate condition?
	if (r0.terminated or r0.stalled) and (r1.terminated or r1.stalled):
		return 1
	else:
		return 0
	
with open("input.txt") as fh:
	cmdlist = fh.readlines()
reg0 = regi(cmdlist,0)
reg1 = regi(cmdlist,1)
itercount = 0
reg1sentdata = 0
while terminatedstate(reg0,reg1) == 0 and itercount < 10000000:
	itercount+=1
	# iterate reg0 until it stalls:
	while not reg0.terminated and not reg0.stalled:
		reg0.operate()
		if reg0.sendflag:
			reg1.addQueue(reg0.sendval)
	# then iterate reg1 until it stalls too:
	# print reg0.registers
	# print reg1.queue
	while not reg1.terminated and not reg1.stalled:
		reg1.operate()
		if reg1.sendflag:
			reg0.addQueue(reg1.sendval)
			reg1sentdata += 1
	# print reg1.registers
	# print reg0.queue
	
print "the whole situation took " + str(itercount) + " operations."
print "reg 1 sent data " + str(reg1sentdata) + " times."
#print reg0.registers
#print reg1.registers

