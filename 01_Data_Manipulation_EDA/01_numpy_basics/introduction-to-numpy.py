import numpy as np

np1 = np.array([1,2,3,4,5,6])
print(np1)

# Shape
print(np1.shape)
# Range
np3 = np.arange(10)
print(np3)

# Step

np4 = np.arange(1,20,2)
print(np4)

# Zeros 
np0 = np.zeros((2,10))
print(np0)

# Full 1 & 2 Dim
np6 = np.full(10,6)
print(np6)
np7 = np.full((2,10), 5)
print(np7)

mylist = [1,2,3,4,5,6]
np8 = np.array(mylist)
print(np8)
print(np8[2])