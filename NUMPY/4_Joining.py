import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

R_arr= np.concatenate((arr1, arr2)) # for axis = 0
print(R_arr)

arr = np.array([[1,20],[1,35]])
arr_p = np.array([[45,5],[7,8]])


R_arr =np.concatenate((arr,arr_p),axis=1) # for axis = 1
print(R_arr)

# If axis = 0 ----> direction of stackng or splitting is vertical
# If axis = 1 ----> direction of stackng or splitting is Horizontal
#If axis = 2 ----> direction of stackng or splitting is depth

a1 = np.stack ((arr1,arr2), axis =1)
print(a1)
print()

a2 = np.hstack((arr1, arr2))

print(a2)
print()

a3 = np.vstack((arr1,arr2))
print(a3)

arr = np.dstack((arr1, arr2))

print(arr)



 