import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([4,5,6,7,8])
print(np.add(x,y)) 

# another way around to add
print(np.sum([x,y])) 
print(np.sum([x,y],axis=0)) # this is at axis 0 (columns)
print(np.sum([x,y],axis=1)) # this is at axis 1 (rows)

# cummulattive sum
print(np.cumsum(x))

# products
print(np.prod(x))
print(np.prod([x,y]))

print(np.prod([x,y],axis=1)) # this is at axis 1 (rows)
# cumproduct/ partial product
print(np.cumprod(x))

# Differences
print(np.diff(x))
# we can do it for 2nd order differences
print(np.diff(x,n=2))

