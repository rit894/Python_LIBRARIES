# NumPy Array Reshaping
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(4,2,-1)
# print(newarr.base)
# print(newarr)
# print(newarr.shape)
# print(arr.ndim)
# print(newarr.ndim)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr1)
# print(arr1.shape)
# newarr1 = arr1.reshape(-1)
# print(newarr1)
# print(newarr1.shape)


# NumPy Array Iterating
# for x in arr:
#     print(x)
# for x in arr1:
#     # print(x)
#     for y in x:
#         print(y)
# print()

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr3:
#     print(x)
#     for y in x:
#         print(y)
#         for z in y:
#             print(z)

# for x in np.nditer(arr3):
#     print(x)

# for i in np.nditer(arr3, flags=['buffered'],op_dtypes=['S']):
#     a = i
#     print(a)
# # Slicing Using nditer
# for i in np.nditer(arr3[:,::2]):
#     print(i)

#  Enumeration with ndenumerate()
for ind , x in np.ndenumerate(arr3):
    print(ind, x)