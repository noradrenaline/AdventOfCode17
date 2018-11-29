# the trick here is going to be to get recursion going in a way that plays nicely 
# with selection from a list with no replacement.
# probably python's set stuff will help?

# parse the input into a set
parts = set()
fhlines = 0
with open("input.txt") as fh:
	for line in fh:
		(a,b) = line.strip().split('/')
		parts.add((int(a),int(b)))
		fhlines += 1 # i know there's a more pythonic way to do this

print("There were " + str(fhlines) + " lines in the input, and you have " + str(len(parts)) + " parts recorded, sound good?")

bestbridge = set()
bestlength = 0
beststrength = 0
bridgelist = {}


def buildBridge(bridgetail,bridgeelems,parts):
	global bestbridge
	global beststrength
	global bestlength
	global bridgelist
	matched = 0
	for part in parts:
		if part[0]==bridgetail or part[1] == bridgetail:
			matched = 1
			newtail = part[1] if part[0]==bridgetail else part[0]
			newelems = bridgeelems.copy()
			newelems.add(part)
			# then recurse
			buildBridge(newtail,newelems,parts-newelems)
	if matched == 0:
		# we have hit an end
		# get this bridge's strength
		bl = len(bridgeelems)
		bs = 0
		for part in bridgeelems:
			bs += part[0] + part[1]
		if bl > bestlength:
			bestlength = bl
			beststrength = bs
			bestbridge = bridgeelems
		elif bl == bestlength and bs > beststrength:
			beststrength = bs
			bestbridge = bridgeelems
		bridgelist[bs] = bridgeelems

buildBridge(0,set(),parts)

print "the best bridge had strength " + str(beststrength) + " and was " + str(bestlength) + " elements long."
print bestbridge
