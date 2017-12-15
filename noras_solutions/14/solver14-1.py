#baseinput = 'flqrgnkx'
baseinput = 'oundnydw'

# use already written code, I put it in a separate file 
# both because it is not new (though slightly modified)
# and so I could play a bit with importing from files I wrote

from regdef import register, hashme

# I'm assuming that they want us to hash by doing 64 repeats as in the previous day, but maybe I'm wrong?
# indeed, and it appears they also want us to append the extra junk - the hash algorithm is 
# EXACTLY as in day 10. 

total = 0
for i in range(128):
	input = baseinput + "-" + str(i)
	h = hashme(input)
	b = "{0:0128b}".format(int(h,16))
	total += sum([int(c) for c in b])

print "number of used squares: " + str(total)
