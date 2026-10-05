import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
# 1-Dim array Shape
print(np1.shape)

# 2-dim array Shape
np0 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np0.shape)

# 2-dim reshape 

np2 = np1.reshape(3,4)
print(np2)
print(np2.shape)

# 3-dim reshape

np3 = np1.reshape(2,3,2)
print(np3)
print(np3.shape)

# Flatten to 1-D
np4 = np3.reshape(-1)
print(np4)

