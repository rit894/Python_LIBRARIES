from numpy import random as ran
import matplotlib.pyplot as plt
import seaborn  as sns

# LOgistic Distribution

x= ran.logistic(loc=1,scale=2,size=(2,3))
print(x)
sns.displot(ran.logistic(size=1000),kind="kde")
# plt.show()

data = {
    "normal": ran.normal(loc=10,scale=1.8,size=1000),
    "logistic": ran.logistic(loc=10,size=1000)
    }
sns.displot(data, kind="kde")
# plt.show()


# MULTINOMIAL DISTRIBUTION
# a generalistion of binomial distribution

x = ran.multinomial(n=6,pvals=[2/6,1/6,1/6,1/6,1/6,0],size=1000)
print(x)
sns.displot(x,kind="kde")
plt.show()

