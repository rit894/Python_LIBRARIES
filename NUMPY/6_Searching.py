import numpy as np
#NumPy Searching Arrays
arr = np.array([1,2,3,4,5,4 , 5, 4, 6 , 9])
x= np.where(arr==4)
print(x)
x = np.where(arr%2 == 0)
print(x)

Arr_sorted = np.array([1,2,3,4,6,8,9])
x = np.searchsorted(Arr_sorted,8)# This methode is used to find the index of particular value to put in the sorted list
print(x)

# to inser multiple values into the array
x=np.searchsorted(Arr_sorted,[7,5,3], side='left')
print(x)