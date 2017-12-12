# the best way to go about solving this that I can think of is to 
# reduce the steps down to only 2 dimensions (possibly 1).

with open("input.txt") as fh:
	steps = fh.read().strip().split(',')

directionmap = {'n':0,'ne':1,'se':2,'s':3,'sw':4,'nw':5}
stepcounts = [0,0,0,0,0,0]
for d in steps:
	stepcounts[directionmap[d]]+=1
# remove easy reversals:
s = [stepcounts[i]-stepcounts[(i+3)%6] for i in range(6)]
ss = map(lambda x: x if x>0 else 0,s)
pos = map(lambda x: x>0,s)
print ss

# okay, the goal is to project this into two adjacent directions (e.g. N and NE).
# the actual projection should be simple, but which two should we pick?
# any two non-opposite directions span the space, but which two get you to the position in the least time?

# there's only 6 possible combinations; for the purposes of this exercise we could guess and check,
# but that feels weird. EDIT: now I'm kind of wishing I had done that instead of the 
# squirrelly nonsense below.

# We are either a Y shape or a C shape.
# If we are a Y shape, the two principle directions will be:
# the longest branch of the Y and the direction in between the longest and second-longest
# if we are a C shape the two principle directions will be the middle direction and the
# longest edge direction. I feel pretty good about those conclusions. So how to map?
# pick the "central" direction. This is either: the middle of a c, or the direction opposite the shortest y
# if there's a tie for the shortest y, just pick one, it will turn out not to matter.
# hmmm, I guess technically we could also end up in a weird position where we're neither in a c nor y
# if, say, one of the directions cancelled out. I happen to know that's not happening in this
# exercise, but I feel bad about not handling it, nevertheless.

hasneighbors = [pos[(i-1)%6]+pos[(i+1)%6] for i in range(6)]
# print hasneighbors
def min_positive_value(arr):
	min = max(arr)
	for val in arr:
		if val < min and val >= 0:
			min = val
	return min
def max_except(arr,idx):
	return max(arr[:idx]+arr[idx+1:])
def find_remaining_axis(arr,idx1,idx2):
	arr[idx1] = False
	arr[idx2] = False
	return arr.index(True)
	
if 1 not in hasneighbors:
	# this is the case where we're a Y (every positive direction has 0 positive neighbor directions
	central_axis_neg = s.index(min_positive_value(s))
	central_axis = (central_axis_neg+3)%6
	other_axis = s.index(max_except(arr, central_axis_neg))
	last_axis = find_remaining_axis(pos,central_axis_neg, other_axis)
else:
	central_axis = hasneighbors.index(2)
	other_axis = s.index(max_except(s,central_axis))
	last_axis = find_remaining_axis(pos,central_axis,other_axis)

if central_axis == other_axis or central_axis == last_axis or other_axis == last_axis:
	print "SHIIIIIIT"
	exit()

# then because of how hex projection works (for the off-axis being smaller than the other two
# we can just add the values at central_axis and other_axis (if we are in the c state) (which we are)
print s[central_axis] + s[other_axis]

def project(value,axis,dir1,dir2):
	# takes a value on an axis and returns its projection onto the two other axes.
	# the axes are as mapped above (n=0,ne=1,etc)
	# do not allow dir1==dir2 (or negative)
	if axis == dir1:
		return [val,0]
	elif (axis+3)%6 == dir1:
		return [-val,0]
	elif axis == dir2:
		return [0,val]
	elif (axis+3)%6 == dir2:
		return [0,-val]
	else:
		# here we have to know if the axes are adjacent: 
		proj = [None,None]
		if abs(axis-dir1) == 1: # THIS IS NOT RIGHT IT DOESN"T HANDLE ROLLOVERS
			proj[0] = val
		else:
			proj[0] = -val
		if abs(axis-dir2) == 1:
			proj[1] = val
		else:
			proj[1] = -val
		return proj
