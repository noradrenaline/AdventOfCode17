# this time we just need to convert the final state back to an array
# and then run, counting, from that starting point

import numpy as np
hexv = list("0edcba886653321a")
v = [int(i,16) for i in hexv]
v = np.asarray(v)

def get_unique_number(v):
	hexstr = ''
	for i in range(len(v)):
		if (v[i]>15):
			print "YOU DONE GOOFED"
			exit()
		else:
			hexstr = hexstr + format(int(v[i]),'x')
	return hexstr

def spread_out_max(v):
	val = max(v)
	idx = np.argmax(v) # this conveniently returns the first one only
	v[idx] = 0
	# there's probably a slick way to do this but what the hey
	while (val > 0):
		idx = (idx+1)%len(v)
		v[idx] += 1
		val -= 1
	return v
d = {}
iters = 0
identifier = get_unique_number(v)
print identifier

while (identifier not in d):
	iters += 1
	d[identifier] = 1
	v = spread_out_max(v)
	identifier = get_unique_number(v)
print "finally: " + str(iters)
print "with identifier " + str(identifier)
