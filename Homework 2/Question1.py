import numpy as np
print "Numpy Version: " , (np.__version__)
import matplotlib.pyplot as plt

# Three Samples
sample1 = np.matrix([1, 3, 1])
sample2 = np.matrix([3, 2, -1])
sample3 = np.matrix([4, 1, -1])

# initial weight (transpose)
weight0 = np.matrix("2; 1; -1")
# 2 - x + y = 0

plt.scatter([1,3,4],[3,2,1])
# plt.show()

print sample1
print sample2
print sample3
print weight0