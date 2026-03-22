#Splitting Arrays
import numpy as np
arr= np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)

newarr = np.array_split(arr,6)
print()
print(newarr)

arr = np.array([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]])
newarr = np.array_split(arr,4)
print()
print(newarr)

## Use array_split which is mosrt preferable than split as it might casue errors if the 
#diven parent array cannot be split int daughter ones.

#NOTE
# There are other splits just like vstack, hstack, dstack



