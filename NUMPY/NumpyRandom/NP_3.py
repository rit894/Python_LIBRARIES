from numpy import random
import numpy as np


arr =np.array([1,2,3,4,5,6])
random.shuffle(arr) # chnges are made to the original array
print(arr)
print()


print(random.permutation(arr))

