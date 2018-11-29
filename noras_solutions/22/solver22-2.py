numsteps = 10000000
pos = [0,0]
bearing = [0,1]
def turn_left(bearing):
	return [-bearing[1],bearing[0]]

def turn_right(bearing):
	return [bearing[1],-bearing[0]]

def turn_around(bearing):
	return [-bearing[0],-bearing[1]]

# get the input in - we just need a hash of points that are already infected.
with open("input.txt") as fh:
	lines = fh.readlines()
y = (len(lines)-1)/2
xstart = -(len(lines[1].strip())-1)/2

def tostr(pos):
	return "x"+str(pos[0])+"y"+str(pos[1])

# populate initial infections:
infections = {}
for line in lines:
	x = xstart
	for char in line.strip():
		if char == "#":
			infections[tostr([x,y])]="i"
		x += 1
	y -= 1
	
infectionsApplied = 0
for _ in xrange(numsteps):
	pstr = tostr(pos)
	if pstr not in infections or infections[pstr] == 'c':
		bearing = turn_left(bearing)
		infections[pstr] = 'w'
	elif infections[pstr] == 'w':
		infections[pstr] = 'i'
		infectionsApplied += 1
	elif infections[pstr] == 'i':
		bearing = turn_right(bearing)
		infections[tostr(pos)] = "f"
	elif infections[pstr] == 'f':
		bearing = turn_around(bearing)
		infections[pstr] = 'c'

	pos[0] += bearing[0]
	pos[1] += bearing[1]
print "after " + str(numsteps) + " bursts, we applied " + str(infectionsApplied) + " infections."



