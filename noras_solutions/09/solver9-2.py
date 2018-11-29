with open("input.txt") as fh:
	input = fh.read().strip()

current_val = 0
in_garby = 0
skipping = 0
score = 0
num_garby = 0
for c in input:
	if skipping:
		skipping = 0
	elif in_garby:
		if c == "!":
			skipping = 1
		elif c == ">":
			in_garby=0
		else:
			num_garby += 1
	elif c == "<":
		in_garby = 1
	elif c == "{":
		current_val += 1
	elif c == "}":
		score += current_val
		current_val -= 1
	elif c == ",":
		# this doesn't really matter
		# wait can you really not have an empty case???
		continue
	else:
		print "I don't think you can get here, so hm."

print "score: " + str(score)
print "number of characters in garby: " + str(num_garby)
