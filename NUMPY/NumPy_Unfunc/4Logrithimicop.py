import numpy as np
from math import log

x=np.arange(1,10)
print(np.log2(x)) # base 2

y=np.arange(1,10)
print(np.log10(y)) # base 10 

z= np.arange(1,15)
print(np.around(np.log(z),decimals=2)) # base e

a = np.frompyfunc(log, 2,1)
print(np.log(100,15))


