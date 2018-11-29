# there's no way that I can simulate this in a reasonable time, I suspect.
# what can I know about the situation here.
# as the values get big, the number of times I have to loop back to the beginning
# get smaller, so for instance, if the 50 millionth insert fell near the end of the 
# thing, I would only need to record the first... 45 million or so.
# that doesn't get me much.

# oh, but I no longer need to keep track of WHAT is in the list, just 
# the most recent number I have inserted when the position was 0.
# that is a much smaller/faster operation. Can I try that?

pos = 0
arrsz = 1
input = 377
ans = 0

for x in xrange(1,50000000):
        pos = (pos+input)%x + 1
	if pos == 1:
		ans = x

print ans
	
