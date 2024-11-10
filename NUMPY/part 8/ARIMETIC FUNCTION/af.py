# ONE dimensional array

# import numpy as np

# var = np.array([1, 2, 3, 4, 5, 3, 2])
# print("Min: " ,np.min(var), np.argmin(var)) # min value and index print
# print("Max: " ,np.max(var), np.argmax(var)) # max value and index print


# TWO Dimensional Array

import numpy as np 
var1 = np.array([[2, 1, 3], [9, 5, 6]])
print(np.min(var1, axis = 1)) # We have two axis => axis 0 and axis 1 ==>> axis 0 works on the column and axis 1 works on the rows