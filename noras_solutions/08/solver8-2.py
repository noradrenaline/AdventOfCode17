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
maxEva = 0 # registers start at 0 so this is the lowest possible max
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
	maxEva = d[arr[0]] if d[arr[0]]>maxEva else maxEva


print "the maximum reg value of all time is " + str(maxEva)
