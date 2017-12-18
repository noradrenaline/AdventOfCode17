# I'm trying to think if there's some clever way to handle this 
# like working backwards or something.
# I mean I guess I can program the first bit of this dumbly.
# I assume that resizing / reallocating an array is as (relatively) 
# slow in python as it was in matlab, but it is so easy!
#input = 3
input = 377
arr = [0]
pos = 0

for x in xrange(1,2018):
	pos = (pos+input)%len(arr) + 1
	arr = arr[:pos]+[x]+arr[pos:]

print arr[pos]
print arr[pos+1];

