import numpy as np
x = np.sin(np.pi/2)
print(x)
arr = np.array([np.pi/2, np.pi/3, np.pi/4])

x= np.rad2deg(arr)
print(x)
print(np.sin(np.deg2rad(x)))

#sin alway expects pi/2 sort of thing so use that only
# to find angles

x= np.arcsin(1.0)
print(np.rad2deg(x))

x= np.array([0.5,-1,1])
print(np.arcsin(x))
print(np.rad2deg(np.arcsin(x)))


base = 3
perp = 4

x = np.hypot(base, perp)

print(x)
