# let's start all the way over because shit, dude.
# okay. Let's agree on two axes to span the space so we can know what the f we're talking about.
# I pick N and NE. This will not always be the most direct way home, however; we'll always have to 
# project to calculate it, but fortunately it's not bad..
#import sys
#mypoint = [int(sys.argv[1]),int(sys.argv[2])]

stepmap = {"n":[1,0],'ne':[0,1],'se':[-1,1],'s':[-1,0],'sw':[0,-1],'nw':[1,-1]}

# for a couple of coordinates, test the distance counter functions.
def dist_default(point):
	return abs(point[0])+abs(point[1])

def dist_ccw_basis(point):
	point[0] = point[0]+point[1]
	point[1] = -point[1]
	return abs(point[0]) + abs(point[1])

def dist_cw_basis(point):
	point[1] = point[1]+point[0]
	point[0] = -point[0]
	return abs(point[0]) + abs(point[1])

#print "mypoint: "
#print mypoint
#print "distance in default basis: " + str(dist_default(mypoint))
#print "distance in ccw basis: " + str(dist_ccw_basis(mypoint))
#print "distance in cw basis: " + str(dist_cw_basis(mypoint))

# okay, now let's step through the whole mamma jamma in the default basis and get the end point. 
# actually, let's solve 11-1 here now that I've built something that presumably works.

with open("input.txt") as fh:
	input = fh.read().strip().split(',')

coords = [0,0]
for dir in input:
	coords[0] += stepmap[dir][0]
	coords[1] += stepmap[dir][1]

print "final coords: "
print coords
print "distance in default basis: " +str(dist_default(coords))
print "distance in ccw basis: " + str(dist_ccw_basis(coords))
print "distance in cw basis: " + str(dist_cw_basis(coords))
