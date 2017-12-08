# so we happen to know that wiapj is the base node.
# let's make a node-weighing method?
# or well, let's make a node class.
import re

class pnode:
	def __init__(self,line):
		arr = line.split()
		self.name = arr[0]
		self.self_weight = int(re.search(r"\d+",arr[1]).group())
		if (len(arr)>2):
			self.children = map(lambda x: x.replace(',',''),arr[3:])
	#		self.total_weight = self.self_weight
		else:
			self.children = []
	#		self.total_weight = -1

#	def total_weight(self):
#		if (len(self.children)==0):
#			return self.self_weight
#		else
#			total_weight = self_weight
#			for child in # crap

# build a dict of these guys: (I think dict is best)
pdict = {}
with open("fakeinput.txt") as fh:
	for line in fh:
		node = pnode(line)
		pdict[node.name] = node
# okay, now let's define a function that recurses the structure, I guess?
def get_total_weight(d,name):
	if (len(d[name].children)==0):
		return d[name].self_weight
	else:
		total_weight = d[name].self_weight
		for child in d[name].children:
			total_weight += get_total_weight(d,child)
		return total_weight

# test on fakedata:
print get_total_weight(pdict,'ugml')

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





