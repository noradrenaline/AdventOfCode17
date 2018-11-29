# be all memory inefficient and just load them all into memory I guess
nodes = {}

with open('input.txt') as fh:
	for line in fh:
		[name,edges] = line.split(" <-> ")
		edgelist = edges.strip().split(', ')
		nodes[name] = edgelist

masterlist = set()
def addToSet (name, nodes, group):
	if name in group:
		return
	else:
		group.add(name)
		for linkedname in nodes[name]:
			addToSet(linkedname,nodes,group)

num_groups = 0
for name in nodes:
	if name not in masterlist:
		num_groups += 1
		zgroup = set()
		addToSet(name,nodes,zgroup)
		masterlist = masterlist | zgroup

print "there were " + str(num_groups) + " groups"
