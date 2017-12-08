import sys
file = sys.argv[1]
with open(file) as fh:
	lines = fh.readlines()

def regEval(reg,comp,val):
	# reg should be the value of the register,
	# i.e. call syntax is going to be checkReturn(dict['abc'],"==",5)
	return eval(str(reg) + comp + str(val))

def touchReg(d,reg):
	if reg not in d:
		d[reg] = 0
	return d

d = {}
for line in lines:
	arr = line.split()
	d = touchReg(d,arr[0])
	d = touchReg(d,arr[4])
	if (regEval(d[arr[4]],arr[5],arr[6])):
		if arr[1] == 'inc':
			d[arr[0]] += int(arr[2])
		elif arr[1] == 'dec':
			d[arr[0]] -= int(arr[2])
		else:
			print "whaaaaatttttttt"
			print arr[1]
			exit()

# then what's the quick way to get the max out of a dict?
maxRegValue = max(d.values())

print "the maximum reg value is " + str(maxRegValue)
