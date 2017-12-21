# can we do anything other than just simulate?
# I feel like there's some funky arithmetic to consider.
# v(t) = v0 + a*t 
# p(t) = p0 + v0*t + a * sum([tt for tt in xrange(t)])
# ^ actually should be xrange t+1 I guess
# oh but that sum is expressible as t*(t+1)/2
# so p(t) = p0 + v0*t + a*t*(t+1)/2
# pixel space is weird by a factor of at/2

# so this means we don't have to track all the intermediate positions, 
# we can just generate them using this equation

# however, this still leaves us simulating, which I don't think I can 
# fully get around. the outstanding question becomes, 
# when do we stop? when do we know that all collision that can ever happen
# have already happened?

# man I can just taste a slick linear algebra solution to this problem,
# but I can't think it up right now. Kind of maddening.

def pos(x,t):
	# x is the 3 initial values in a dimension
	return x[0]+x[1]*t+x[2]*t*(t+1)/2 
	# t(t+1) is always even so I don't care about 
	# fucking weird ass integer division anyway.

# still doesn't help with the whole "when are we done" issue.
# if we want to know whether 2 particles will ever collide,
# we solve for t where x1(t)=x2(t) and y1(t) = y2(t) and z
# (t>0 of course)
# I'm picturing an approach where we narrow it down by manually checking
# for collisions for the first, idk, 10k iterations? 
# and then what, check for collisions anywhere in the future by solving the 
# overconstrained equations above? 
# that would be how we knew for sure that we didn't miss any future collisions,
# but if we have a lot of particles it could get kind of costly.
# IDK there's only 1000 particles to begin with.

# let's start by eliminating any that we can by simulation, I guess?

with open("input.txt") as fh:
	plines = fh.readlines();

class particle:
	def __init__(self,pline):
		[p,v,a] = pline.strip().split(", ")
		[px,py,pz] = [int(u) for u in p[3:-1].split(',')]
		[vx,vy,vz] = [int(u) for u in v[3:-1].split(',')]
		[ax,ay,az] = [int(u) for u in a[3:-1].split(',')]
		self.x = [px,vx,ax]
		self.y = [py,vy,ay]
		self.z = [pz,vz,az]
		self.removed = 0
	def locate(self,t):
		xt  = self.x[0]+self.x[1]*t+self.x[2]*t*(t+1)/2
		yt  = self.y[0]+self.y[1]*t+self.y[2]*t*(t+1)/2
		zt  = self.z[0]+self.z[1]*t+self.z[2]*t*(t+1)/2
		return [xt,yt,zt]
	def locate_descriptive(self,t):
		pos = self.locate(t)
		return "x" + str(pos[0]) + "y" + str(pos[1]) + "z" + str(pos[2])

# this class should give us what we need to iterate/simulate.
# well, let's build our list of particle objects
particleMan = [particle(i) for i in plines]

print "first guy at t0"
print particleMan[0].locate_descriptive(0)
print "and at t1"
print particleMan[0].locate_descriptive(1)

# okay so that all works out. Now, the last bit is that for a given time 
# we need to be able to eliminate the particles.
totalparticles = len(particleMan)

for t in xrange(10000):
	locations = {}
	for i,p in enumerate(particleMan):
		if p.removed:
			continue
		lstr = p.locate_descriptive(t)
		if lstr in locations:
			# remove both p and the one who is already in that location:
			particleMan[i].removed = 1
			particleMan[locations[lstr]].removed = 1
		else:
			locations[lstr] = i
	
	if t%100 == 0:	
		numRem = sum([p.removed for p in particleMan])
		print "t = " + str(t)
		print "particles left: " + str(totalparticles-numRem)






# wellllllllllll, this is the laziest thing ever but we seem to have converged
# on an answer. I am justifying this by an order of magnitude argument that
# the starting positions are within 10k of 0 pretty universally, and the scale
# factor of the acceleration is at least 1, so that the particles will disperse 
# pretty thoroughly within the first couple thousand, but this is a pretty 
# intuition-based argument, I have not proven it rigorously to myself.









