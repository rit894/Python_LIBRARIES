# numpy Data types
import numpy as np
arr = np.array([1, 2, 3, 4, 5], dtype='S')
# print(arr.dtype)
# print(arr[1]+arr[2])
# arr1 = np.array(['a', '2'], dtype='i') // shows errors


arr1 = np.array([4,1.2,1.3],dtype='int')
# print(arr1.dtype)
newarr  = arr1.astype(bool)
# print(newarr)
# print(newarr.dtype)

# The Difference Between Copy and View
arr2 = np.array([1,2,3,4,5])
x = arr2.copy()
y= arr2.view()
y[0]=0
arr2[0]=12


# print(arr2)
# print(x.base)
# print(y.base)

# NumPy Array Shape
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3.shape)

arr4 = np.array([1,2,3,4,5], ndmin=5)
# print(arr4)
# print(arr4.shape)