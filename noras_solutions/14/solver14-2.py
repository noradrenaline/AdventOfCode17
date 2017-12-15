# if it were MATLAB I would use the image/connectedcomponents tool
# I'm sure Python has similar, but this is advent of code so let's code.
#baseinput = 'flqrgnkx'
baseinput = 'oundnydw'

from regdef import register, hashme
import numpy as np

pic = np.zeros((128,128))
for i in range(128):
	input = baseinput + "-" + str(i)
	h = hashme(input)
	b = "{0:0128b}".format(int(h,16))
	pic[i,] = [int(c) for c in b]

	
pic = -1*pic
fourlist = [np.array([-1,0]),np.array([0,-1]),np.array([1,0]),np.array([0,1])]
def connect_four(pic,num,coords):
	# if the coord is -1, paint it and everything it touches num
	if pic[coords[0],coords[1]] < 0:
		pic[coords[0],coords[1]] = num
		# and then also paint the 4-connecteds
		# don't run off the grid tho:
		for dc in fourlist:
			nc = coords+dc
			if min(nc)>=0 and max(nc)<128:
				pic = connect_four(pic,num,nc)
	
	return pic


for x in range(128):
	for y in range(128):
		n = np.amax(pic) + 1
		coords = np.array([x,y])
		connect_four(pic,n,coords)
print pic[:8,:8]
print "max group number:"
print np.amax(pic)
