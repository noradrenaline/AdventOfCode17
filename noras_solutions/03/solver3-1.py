# is there a less dumb way to do this than to just iterate?
# well, what would be the rules for iterating?

# if x>=0 and y>0 attempt to move left, failing that move up
# if y>=0 and x<0 attempt to move down, failing that move left
# if x<=0 and y<0 attempt to move right, failing that move down
# if y<=0 and x>0 attempt to move up, failing that move right

# then we need a way to keep track of if we can move into a space or if it's already occupied
# one could hypothetically build the whole dang matrix but that is probably wasteful
# it suffices to keep track of the corners of the rectangle, right?
# WOAH HOLD THE PHONE, the bottom right corner is n**2 with n odd.
# because that point is when you complete the odd-sided square.

# So okay. Floor of square root of the input gives us the x/y coordinates of 
# a relatively recent entry. Then we just have to count where we are from there 
# in terms of the traversal around the square.
import math

input = 289326
#input = 9

nextsquare = math.ceil(input**(1./2)) 
# ^ this is the dumbest thing I've ever seen in my whole life
# like seriously are you shitting me with that shit
# 1/2=0 in this godforsaken language what the fuck

# btw it has to be the next odd square
nextsquare = nextsquare + (1-nextsquare%2)

# fucking where were we.

# so now we know that the farthest it can be is nextsquare-1 (if it's on a corner)
# the closest it can be is (nextsquare-1)/2 (if it's on one of the axes)

lastsquare = nextsquare - 2

# we know that the value is between lastsquare and nextsquare.
# we can tell where along a side we are by counting up from lastsquare

sideprogress = (input-lastsquare**2)%(nextsquare-1)

# each step takes one off the max possible total distance of (nextsquare-1)
# until you get to the halfway point, at which point you add back on
# what's a graceful way to handle that? Distance from half?

base = (nextsquare-1)/2
additional = abs((nextsquare-1)/2 - sideprogress)

distance = base+additional
print distance





