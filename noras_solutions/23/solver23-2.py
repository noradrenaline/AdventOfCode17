# so the thing that triggers h to change value is f being 0 at that point in the program.
# and the thing that triggers us to actually escape is b = c when we get to that point.
# so we just need to figure out how many iterations of the code between the setup of b and c
# Looking at the values tha b and c get set up as, it looks like we have to hit the 2nd to last line
# 1000 times (it will exit on the 1001st time, unless I'm off by one)
# I don't really care what has to happen to get us past that gnz g -13, just that it has to happen
# 1001 times, right?
# oh shit, but there's that f-based skip right before sub h -1. That means that h only gets subtracted
# when f is 0, which only happens when g was 0 in the previous round, which is when?

# basically, there are two loops, both controlled by g: the jnz g -8 at line 19 and the -13 at line 23.
# If I can simplify the operation of those loops and see if I can predict the state of f each time we
# escape the loops, that will inform what happens to h.

# oh jeez. I think I see what question this is attempting to answer. It is looping through from 2 to b
# across all #s, twice, and, if two numbers in that range multiply to b, it sets f = 0. In other words, 
# if b is NOT prime then it will increment h. It does this for b from 109300 to 126300 in steps of 17 
# (checking 1000 numbers in all).
# let me just get a list of primes up to 126300/2 = 63150 I guess?

# then I can just loop those 1000 numbers, check if any of them are prime.
# jeez.

# what are my edge conditions? It DOES check 109300 (which is not prime, obvi)
# but it will ALSO check 126300.

primelist = set()
with open("primes.txt") as fh:
	for line in fh:
		for p in line.split():
			primelist.add(int(p))

def testcomposite(b,pl):
	for p in pl:
		if b%p == 0:
			return 1
	return 0

# then just loop the numbers.
b = 109300
numcompostie = 0 # I like this typo, keeping it
while b <= 126300:
	print "testing " + str(b)
	numcompostie += testcomposite(b,primelist)
	b += 17

print "found " + str(numcompostie) + " poop-garbage compost-y nonprimes."


