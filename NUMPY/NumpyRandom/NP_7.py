from numpy import random as ran
import seaborn as sns
import matplotlib.pyplot as plt


x = ran.exponential(scale=2,size=1000)
# print(x)

sns.displot(ran.exponential(scale=2,size = 1000),kind ='kde')
plt.show()

data ={
    "possion":ran.poisson(lam=2,size=1000),
    "Exponential":ran.exponential(scale=2,size=1000)
}

sns.displot(data,kind='kde')
plt.show()