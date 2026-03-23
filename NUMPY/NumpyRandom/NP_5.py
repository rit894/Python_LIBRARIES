from numpy import random as ran
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# POISSION DISTRIBUTION
#It estimates how many times an event can happen in a specified time.
# e.g. If someone eats twice a day what is the probability he will eat thrice?

x= ran.poisson(lam=2,size=1000)
print(x)

sns.displot(ran.poisson(lam=2,size=1000))
# plt.show()

data={
    
    "normal":ran.normal(size=1000,loc=50,scale=7),
    "poisson":ran.poisson(lam=50,size=1000),
    
}
sns.displot(data,kind="kde")
# plt.show()

# UNIFORM DISTRIBUTION
x =ran.uniform(size=(2,3))
print(x)

sns.displot(ran.uniform(size=1000), kind="kde")
plt.show()