# we just need to look at the ones with the smallest acceleration
# so let's find the smallest acceleration, and see how many particles
# share that acceleration.

# is there a read line generator that I could loop? That would be more efficient.
with open("input.txt") as fh:
	plist = fh.readlines()

minval = 1000000 # by visual inspection, this is larger than the actual min a
minps = []

for i, p in enumerate(plist):
	[_,_,a] = p.strip().split()
	a_s = a[3:-1].split(',')
	[x,y,z] = [int(a) for a in a_s]
	a_c = abs(x)+abs(y)+abs(z)
	if a_c < minval:
		minval = a_c
		minps = [i]
	elif a_c == minval:
		minps += [i]

print "minimum value " + str(minval)
print minps

