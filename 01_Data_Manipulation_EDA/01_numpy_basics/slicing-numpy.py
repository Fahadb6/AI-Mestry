import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9])
# Return 2,3,4,5
print(np1[1:5])

# Return 4-9
print(np1[3:])

# Return Negative Num
print(np1[-3:-1])

# Comeback to steps
print(np1[1:5]) # 2-5
print(np1[1:5:2]) # 2-5 in steps 2 

# Steps in  all array
print(np1[::2])

# steps in 2-dim array 
np2 = np.array([[1,2,3,4,5] , [6,7,8,9,10]])
print(np2[1,2])

# one array
print(np2[0:1 , 1:3])

# two array 
print(np2[0:2 , 1:3])
