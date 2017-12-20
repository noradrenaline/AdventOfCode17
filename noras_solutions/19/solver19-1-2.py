with open("input.txt") as fh:
	maze = fh.readlines()
# pad the x-direction
maze = [' ' + i.rstrip("\n") + ' ' for i in maze]
while len(maze[-1]) < len(maze[0]):
	maze.pop()
maze = maze + [" "*len(maze[0])]
# pad the last row - no need on top, but:
maze = [list(i) for i in maze]

def printPos(y,x,maze):
	print "_"*(len(maze[0])+2)
	tmp = maze[y][x]
	maze[y][x] = "X"
	for i in maze:
		print "|"+''.join(i)+"|"
	print "*"*(len(maze[0])+2)
	maze[y][x] = tmp

# annnnyway where was I

x = maze[0].index('|')
y = 0
bearing = [1,0] # defining down as positive because yeah
# note that coordinates will be like [-y,x] because of how it is.
# y is the row index, x is the column
letters = ''
xmax = len(maze[0])
ymax = len(maze)
print "Traversing your " + str(xmax) + " by " + str(ymax) + "maze."
stepsTaken = 0;
while x>=0 and x<xmax and y>=0 and y<ymax:
	stepsTaken += 1
	# printPos(y,x,maze)
	# check for letter
	if maze[y][x].isalnum():
		letters += maze[y][x]
	# check for whitespace/error
	elif maze[y][x] == " ":
		print "encountered the end"
		stepsTaken -= 1
		break
	# check for turn signal
	elif maze[y][x] == "+":
		# it will for sure be a 90 degree turn
		if bearing[0] == 0:
			bearing[1] = 0
			if maze[y+1][x] == ' ':
				bearing[0] = -1
			else:
				bearing[0] = 1
		else:
			bearing[0] = 0
			if maze[y][x+1] == ' ':
				bearing[1] = -1
			else:
				bearing[1] = 1
	
	y += bearing[0]
	x += bearing[1]
		
print letters
print "Steps: " + str(stepsTaken)
