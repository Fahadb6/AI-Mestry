import numpy as np

# np0 = np.array([1,2,3,4,5,6,7,8,9,10])
# for _ in np0:
#   pass

# np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# for i in np2:
#   for x in i:
#     print(x)

np3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
# for i in np3:
#   for m in i:
#     for z in m:
#       print(i)
for x in np.nditer(np3):
  print(x)

print('Hello')