import numpy as np

var = np.array([[1, 2], [3, 4]])
var1 = np.array([[9, 8], [7, 6]])

ar = np.concatenate((var, var1), axis = 1)
print(var)
print()
print(var1)
print()
print(ar)