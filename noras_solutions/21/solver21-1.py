# I'm picturing some sort of a tree structure to look up what pattern you match.
# like: level 1 - size
# 	level 2 - number of on pixels
#	level 3 - either just the list of rotated matches or more specificity. hm.
# we can also have an intermediate map so we don't have to have 4 copies of every
# output frame in memory, which seems slightly friendlier I guess.

# then it's just a matter of doing it.

# yeah, a lot of the fiddling here is going to be prepping the input. 
# each source will have as many as 8 templates.
# the 8 templates are: original+3 rotations+flip+3 rotations of that.
# we can build some maps. Start with the 2x2 case:
r2 = [[0,1,2,3],[1,3,0,2],[3,2,1,0],[2,0,3,1],[1,0,3,2],[0,2,1,3],[2,3,0,1],[3,1,2,0]]
# ^ note that these read top to bottom, left to right, similar to inputs
r3 = [[0,1,2,3,4,5,6,7,8], [2,5,8,1,4,7,0,3,6],[8,7,6,5,4,3,2,1,0],[6,3,0,7,4,1,8,5,2],
	[2,1,0,5,4,3,8,7,6],[0,3,6,1,4,7,2,5,8],[6,7,8,3,4,5,0,1,2],[8,5,2,7,4,1,6,3,0]]

# use of these: neworder = [order[i] for i in r3[n]] for each n

patterns = {} # map all rotations to their line # 
outputs = {} # map line number to output
with open("input.txt") as fh:
	for i, line in enumerate(fh):
		[template,result] = line.strip().split(" => ")
		# first let's handle the output.
		# I think we may actually want to keep this in a square shape.
		newblock = [list(s) for s in result.split("/")]
		# now we have a properly-shaped list o'lists for later joining
		# map it to the line number
		outputs[i] = newblock		

		# get rid of the slashes, don't need em
		template = template.translate(None,'/')
		# map all template permutations to the line number:
		if len(template) == 4:
			for perm in r2:
				variant = ''.join([template[o] for o in perm])
				patterns[variant] = i
		elif len(template) == 9:
			for perm in r3:
				variant = ''.join([template[o] for o in perm])
				patterns[variant] = i
		else:
			print "unexpected template length encountered: " + template
			exit()

# okay, so now we have patterns to match (in the form of string dict entries)
# and output patterns to consume.

# let's set up the initial board:
board = [['.','#','.'],['.','.','#'],['#','#','#']]

# okay, the last two steps will be how to split up a board into chunks, and
# how to combine chunks back into a new board.

# to split a board.
def give_me_chunk(board,n):
	# returns the nth chunk of the board,
	# but in a nice string to use for searching the dict we built.
	# first, are we chunking into 2x2 or 3x3?
	c = 2 if len(board)%2==0 else 3
	cdim = len(board)/c
	if n >= cdim**2:
		# we have asked for a nonexistent chunk
		return 0
	# get starting row:
	row = (n/cdim)*c # that integer division tho
	col = (n%cdim)*c
	# so now pull the rows/columns we need
	return ''.join([''.join(board[r][col:col+c]) for r in range(row,row+c)])
	
#print give_me_chunk(board,0)

# now we can pull chunks which can readily be mapped to new bigger chunks, 
# we need to loop them and re-combine.
# man i miss matlab. (anyone reading this take a shot)

def iterate_board(board,patterns,outputs):
	# define some numbers.
	c = 2 if len(board)%2==0 else 3
	cdim = len(board)/c
	chunkarray = [give_me_chunk(board,n) for n in range(cdim**2)]
	# then we just need to look it up and reshape it
	# fidddddddlyyyyyyy
	# i almost just want to preallocate here just to make my damn life easier
	# lets
	nblen = (c+1)*cdim
	newboard = [['-' for _ in range(nblen)] for _ in range(nblen)]
	# then, ah dang, we could loop or what the fuck ever, man.
	# this is dumb but I'm jammed up trying to make it pythonic or whatever
	# just fucking go
	for crow in range(cdim):
		for ccol in range(cdim):
			chunk = outputs[patterns[chunkarray[crow*cdim + ccol]]]
			for irow in range(c+1):
				for icol in range(c+1):
					newboard[crow*(c+1)+irow][ccol*(c+1)+icol] = chunk[irow][icol]
	return newboard

	
#let's see it work for 2 iterations on fakeinput:
def print_board(board):
	for r in board:
		print ''.join(r)
	print "\n"

print_board(board)
for i in xrange(5):
	board = iterate_board(board,patterns,outputs)
	print_board(board)

# i have lost it entirely, python stopped working for me. fffffffffff
numfull = 0
for row in board:
	for col in row:
		if col == "#":
			numfull += 1
print "number of full spaces: " + str(numfull)








