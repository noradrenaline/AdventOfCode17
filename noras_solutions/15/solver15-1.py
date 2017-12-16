g1 = 516
g2 = 190
a = 16807
b = 48271
nummatch = 0
reps = 40000000
for _ in range(reps):
	g1 = (g1*a)%2147483647
	g2 = (g2*b)%2147483647
	if g1%65536==g2%65536:
		nummatch += 1

print nummatch
