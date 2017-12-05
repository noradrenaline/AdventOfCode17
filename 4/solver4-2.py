fh = open('input.txt','r')

def UNACCEPTABLE(line):
	wordlist = line.split()
	for i in range(len(wordlist)):
		for j in range(len(wordlist)):
			if (i!=j and ''.join(sorted(wordlist[i]))==''.join(sorted(wordlist[j%len(wordlist)]))):
				return 1
	return 0

rejects = 0
for cnt, line in enumerate(fh):
	if (UNACCEPTABLE(line)):
		rejects += 1

print "of " + str(cnt+1) + " rows, " + str(rejects) + " were unacceptable."
print "this leaves " + str(cnt+1-rejects) + " rows OK"

fh.close() # you happy guys? I closed it.
