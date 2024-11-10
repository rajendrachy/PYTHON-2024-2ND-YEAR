import numpy as np
l = []
for i in range(1,5):
    int_1 = int(input("Enter a value : ")) # using int -->> give an integer value
                                            # without using int -->> string value written
    l.append(int_1)

print(np.array(l))
print(type(np.array(l)))    

