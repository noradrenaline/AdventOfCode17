# be all memory inefficient and just load them all into memory I guess
nodes = {}
with open('input.txt') as fh:
	for line in fh:
		[name,edges] = line.split(" <-> ")
		edgelist = edges.strip().split(', ')
		nodes[name] = edgelist

# then build a set, a set right?

# how dumb to be.

# OH THEY TRYNA TRAP US in a loop

zgroup = set()
def addToSet (name, nodes, group):
	if name in group:
		return
	else:
		group.add(name)
		for linkedname in nodes[name]:
			addToSet(linkedname,nodes,group)
addToSet('0',nodes,zgroup)
print len(zgroup)
