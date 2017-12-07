import numpy as np
import math
input = 289326
# input = 800
# this spirals in the wrong direction but that doesn't actually matter.

class Grid:
	
	def __init__(self, offset):
		# please provide an offset that is big enough to not overflow.
		# ceil(sqrt(input)/2) should be safe
		self.offset = offset
		self.space = np.zeros((2*offset+1,2*offset+1))
		self.space[offset,offset] = 1
		self.space[offset,offset+1] = 1
		self.coords = (offset,offset+1) # equivalent to 0,1
		self.numsteps = 1
		
	def currentVal(self):
		return self.space[self.coords]
	
	def iterate(self):
		# which way should we advance?
		self.step()
		self.space[self.coords] = self.sum8connected()
		self.numsteps = self.numsteps+1 # why does ++ not work?		

	def step(self):
		# define x and y for convenience
		offset = self.offset
		y = self.coords[0]-offset
		x = self.coords[1]-offset
		# determine new coords:
		if (x>0 and y>=0):
			# try to go x-1, if unavailable go y+1
			if (self.space[y+offset,x-1+offset]==0):
				#self.coords[i]--
				self.coords = (y+offset,x-1+offset)
			else:
				#self.coords[0]++
				self.coords = (y+1+offset,x+offset)
		elif (x<=0 and y>0):
			# try to go y-1, if unavailable go x-1
			if (self.space[y-1+offset,x+offset]==0):
				self.coords = (y-1+offset,x+offset)
			else:
				self.coords = (y+offset,x-1+offset)
		elif (x<0 and y<=0):
			# try to go x+1, if unavailable go y-1
			if (self.space[y+offset,x+1+offset]==0):
				self.coords = (y+offset,x+1+offset)
			else:
				self.coords = (y-1+offset,x+offset)
		elif (x>=0 and y<0):
			# try to go y+1, if unavailable go x+1
			if (self.space[y+1+offset,x+offset]==0):
				self.coords = (y+1+offset,x+offset)
			else:
				self.coords = (y+offset,x+1+offset)
		else:
			print "invalid: x=" + str(x) + " y=" + str(y)

	def sum8connected(self):
		val = 0
		for i in range(-1,2):
			for j in range(-1,2):
				val += self.space[self.coords[0]+i,self.coords[1]+j]
		return val
	


# determine safe offset:
situation = Grid(int(math.ceil(input**(.5))))

# noisy for testing
while (situation.currentVal() <= input):
	situation.iterate()
	#print "numsteps: " + str(situation.numsteps)
	#print "current val: " + str(situation.currentVal())
	#print "situation:"

print "the first value written that is larger than " + str(input) + " is " + str(situation.currentVal())
# I think that will work?
