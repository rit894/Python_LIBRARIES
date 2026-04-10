import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([4,5,6,7,8])
print(np.lcm(x,y))
print(np.lcm.reduce(x))

x= np.arange(1,11)
print(np.lcm.reduce(x))

# GCD
print(np.gcd.reduce(x))