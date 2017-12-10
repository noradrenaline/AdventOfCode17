# note that the highest possible digit is 15, which means that we can use
# a hexadecimal number to represent a unique combination
# (rather than having to store/compare the array)
# Then we just have to check whether the number is already seen or not.
import numpy as np
v = np.loadtxt("input.txt",delimiter="\t")

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
