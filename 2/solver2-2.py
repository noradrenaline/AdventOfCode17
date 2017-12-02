import numpy as np
mat = np.loadtxt("input.txt", delimiter="\t")

# matlab i miss youuuuuuuuuu
# fuck it i'll write a goddamn loop

total = 0
for u in range (0,mat.shape[0]):
	v1 = mat[u,:]
	v1 = v1[:,np.newaxis] # bestow a second dimension
	v2 = 1/v1.transpose()
	m1 = v2*v1
	verdict = (m1%1==0) - np.eye(m1.shape[0])
	verdict = verdict>0 # there can be -1s due to machine error in self-divides
	value = sum(sum(np.multiply(m1,verdict)))
	if (value == 0):
		# the dumb thing I have to do to handle the case where there's no value due to machine error
		# is it better to filter and only check the filtered matches, or to check everybody?
		# fuck it, we're doing the dumb thing, let's just dumb.
		for i in range (0,v1.size):
			for j in range (0,v1.size):
				# skip i==j
				if (i != j):
					test = v1[i,0]/v1[j,0] # %$#%$#@^#!&%@#
					if (test%1==0):
						value = test
						break
	print np.argwhere(verdict)
	print value
	total += value# sum(sum(np.multiply(m1,verdict)))

print "grand total:"
print total

# grumbles something about matlab
