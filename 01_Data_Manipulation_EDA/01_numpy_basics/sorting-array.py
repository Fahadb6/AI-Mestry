import numpy as np

# Numbers :
np1 = np.array([6,7,4,9,2,4,1,3 ,4,12,11,45,56,65,87,8,9,7,6])
print(np.sort(np1))

# Alpha
np_names = np.array(['Fahad' , 'Ahmed' , 'Salem' , 'Naser'])
print(np.sort(np_names))

# it's so easy 

# Where , search about it 

y = np.where(np1 % 2 == 0)
z = np.where(np1 % 2 ==1)
# print(np1)
# print(y[0])
# print(z[0])


# Filtter in Numpy this is long way to filter
filterd = []
for thing in np1:
  if thing % 2 == 0 :
    filterd.append(True)
  else:
    filterd.append(False)

print(np1)
print(filterd)
print(np1[filterd])

# shourtcut filter
filterd2 = np1 % 2 == 0 
print(np1)
print(filterd2)
print(np1[filterd2])