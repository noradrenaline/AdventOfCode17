import numpy as np
mat = np.loadtxt("input.txt", delimiter="\t")

print sum(mat.max(1)-mat.min(1))



