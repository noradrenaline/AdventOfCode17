class mazeState:
	def __init__(self,filepath):
		with open (filepath,'r') as fh:
			input = fh.read()
		self.maze = [int(i) for i in input.split()]
		self.position = 0
		self.numsteps = 0
	def show_maze(self):
		print self.maze
	def still_trapped(self):
		if (self.position >= len(self.maze) or self.position < 0):
			return 0
		else:
			return 1
	def step(self):
		currentStep = self.maze[self.position]
		self.maze[self.position] += 1
		self.position += currentStep
		self.numsteps += 1

myMaze = mazeState("input.txt")

while (myMaze.still_trapped()):
	myMaze.step()

print "escaped after " + str(myMaze.numsteps) + " steps"
