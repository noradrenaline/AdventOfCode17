numsteps = 10000
pos = [0,0]
bearing = [0,1]
def turn_left(bearing):
	return [-bearing[1],bearing[0]]

def turn_right(bearing):
	return [bearing[1],-bearing[0]]

# get the input in - we just need a hash of points that are already infected.
with open("input.txt") as fh:
	lines = fh.readlines()
y = (len(lines)-1)/2
xstart = -(len(lines[1].strip())-1)/2

def tostr(pos):
	return "x"+str(pos[0])+"y"+str(pos[1])

# populate initial infections:
infections = set()
for line in lines:
	x = xstart
	for char in line.strip():
		if char == "#":
			infections.add(tostr([x,y]))
		x += 1
	y -= 1
	
infectionsApplied = 0
for _ in xrange(numsteps):
	if tostr(pos) in infections:
		bearing = turn_right(bearing)
		infections.remove(tostr(pos))
	else:
		bearing = turn_left(bearing)
		infections.add(tostr(pos))
		infectionsApplied += 1
	pos[0] += bearing[0]
	pos[1] += bearing[1]
print "after " + str(numsteps) + " bursts, we applied " + str(infectionsApplied) + " infections."



