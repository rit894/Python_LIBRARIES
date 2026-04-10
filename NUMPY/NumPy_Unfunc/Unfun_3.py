# ROunding decimals 
import numpy as np
x= np.array([1.23456789,2.3456789,3.456789])
print(np.trunc(x))

# another methode similarly is fix 
print(np.fix(x))

# rounding with around a little efficient as it does increment 
# base on preceding element alone
print(np.around(x,decimals=1))

# similarly we do for floor and ceil functions

print(np.floor(x))
print(np.ceil(x))