# try to solve this analytically, or at least partly so.
# in the test data, row 0 is clear so long as delay%3!=0
# row 1 is clear so long as (delay+1)%2!=0
# SHIT THAT IS NOT RIGHT

# you escape for row 0 so long as delay%(2*range-2)!==0
# row 1: (delay+1)%(2*range-2) != 0

scanners = {}
with open("input.txt") as fh:
	for line in fh:
		(d,r) = line.split(": ")
		scanners[int(d)] = int(r)

def doIescape(scanners,delay):
	for dep in scanners:
		if (delay+dep)%(2*scanners[dep]-2) == 0:
			return 0
	return 1

for delay in range(10000000):
	if doIescape(scanners,delay):
		print "escaped at delay " + str(delay)
		break



