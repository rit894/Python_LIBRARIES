# unfunc Stands for universal functions
import numpy as np
x=[1,2,3,4,5,]
y = [4,5,6,7,8]
z= np.add(x,y)
print('this is addition')
print(z)

def myadd(x,y):
    return x*y
myadd=np.frompyfunc(myadd,2,1)
print('this is multiplication')
print(myadd([1,2,3,4,5],[4,5,6,7,8]))

print(type(myadd))
print(type(np.concatenate))
