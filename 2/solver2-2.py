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
	value = sum(sum(np.multiply(m1,verdict)))
	print np.argwhere(verdict)
	print value
	total += sum(sum(np.multiply(m1,verdict)))

print "grand total:"
print total

# grumbles something about matlab
