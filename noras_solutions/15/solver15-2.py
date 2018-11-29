g1 = 516
g2 = 190
a = 16807
b = 48271
nummatch = 0
comps = 0
totcomps = 5000000
while comps < totcomps:
	comps += 1
	# iterate each generator once to get us started
	g1 = (g1*a)%2147483647
	g2 = (g2*b)%2147483647
	while g1%4 != 0:
		g1 = (g1*a)%2147483647
	while g2%8 != 0:
		g2 = (g2*b)%2147483647
	if g1%65536==g2%65536:
		nummatch += 1

print nummatch
