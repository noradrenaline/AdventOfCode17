import re

# okay, for problem 1 all we really want is the following:
# parse the name of the node program from a line of the list
# if the program has no children, then it's definitely not the base.
# if it does have children, see whether it is itself a child
# (do this by searching the file for \sname[,|\n|$]
# this is the first time I've really been tempted to use perl)

# actually, to be more efficient, once you find the parent here, 
# you can use it in the next search. That will ensure you trace the tree
# down, and not just randomly check all nodes
# here, import each line into an array:
with open(input.txt) as fh:
	lines = fh.readlines()

def findparent(child,line):
	# require a space before child so we don't find our own node
	return re.search(r"\s" + child + r"\b",line)
