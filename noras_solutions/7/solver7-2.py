# so we happen to know that wiapj is the base node.
# let's make a node-weighing method?
# or well, let's make a node class.
import re
import sys
# 0 for test, 1 for real data.
mode = int(sys.argv[1])
file = "fakeinput.txt"
base_node = "tknk"
if mode:
	file = "input.txt"
	base_node = "wiapj"

class pnode:
	def __init__(self,line):
		arr = line.split()
		self.name = arr[0]
		self.self_weight = int(re.search(r"\d+",arr[1]).group())
		if (len(arr)>2):
			self.children = map(lambda x: x.replace(',',''),arr[3:])
			self.total_weight = -1
		else:
			self.children = []
			self.total_weight = self.self_weight

#	def total_weight(self):
#		if (len(self.children)==0):
#			return self.self_weight
#		else
#			total_weight = self_weight
#			for child in # crap

# build a dict of these guys: (I think dict is best)
pdict = {}
with open(file) as fh:
	for line in fh:
		node = pnode(line)
		pdict[node.name] = node
# okay, now let's define a function that recurses the structure, I guess?
def get_total_weight(d,name):
	if (d[name].total_weight ==-1):
		total_weight = d[name].self_weight
		for child in d[name].children:
			total_weight += get_total_weight(d,child)
		d[name].total_weight = total_weight
	return d[name].total_weight

# test on fakedata:
print get_total_weight(pdict,base_node)

# so now we can get the weight of each node.
# we need to figure out how to traverse the tree
# starting from the base, we can trace the issue up the tree based on 
# the "one of these things is not like the others" principle
# I forsee several ambiguities: if a parent node has only one child
# and one of that pair is the error, it would be impossible to determine which one
# had the issue. However, it does not appear that any parents in this set have only one child.
# the more pressing issue is what short-term decision to make when travelling up the tree
# at a node with only two children; we can't use the "one of these things" rule
# in that case, we will need to instead decide which branch to take by checking which 
# grandchildren disagree.
# but (1) if both children are terminal, then what?
# if none of the grandchildren are terminal, then what?

# I want to think about this a little more.

# So okay, now in theory if I run get_total_weight once (on the root node) 
# then I will have all the total_weights.
# I can also keep track of whether each node's children are balanced or not
# then I just trace out to the last node with unbalanced children

# quick sanity check, let me run this on the real input data and make sure it completes
# in a reasonable amount of time.
#print get_total_weight(pdict,'ifyzcgi')
#print get_total_weight(pdict,'wiapj')

# so far, pretty fast.

def is_balanced(d,name):
	# a node is balanced if all its children weigh the same, or if it has no children
	# what's the quickest way to tell if it's balanced? 
	#If the sum of the weights is equal to the number of children times any one weight.
	if (len(d[name].children)>0):
		tots = 0
		for child in d[name].children:
			tots += d[child].total_weight
		return 1 if d[d[name].children[0]].total_weight*len(d[name].children) == tots else 0
	else:
		return 1

# okay, so we can now find the off-balance path.
# start with the base node, find out which children are unbalanced:
wobbly = 1 # base node must be wobbly
node = base_node
while wobbly:
	wobbly = 0
	for child in pdict[node].children:
		if not is_balanced(pdict,child):
			wobbly = 1
			node = child

# at the end here, node should be the last wobbly node; all of its children are balanced.
# this means that one of its children should have its weight changed.
print "the last wobbly node is " + child
print "here are it's children's total weight:"
for child in pdict[node].children:
	print child + " total: " + str(pdict[child].total_weight) + "; individual weight: " + str(pdict[child].self_weight)

print "picking the off child is left for an exercise for the human, i'm sleepy."


