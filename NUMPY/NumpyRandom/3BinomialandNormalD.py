import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as ran

# sns.displot([0,1,2,3,4,4],kind="kde")
# plt.show()

x= ran.normal(size=(2,3))
print(x)

x=ran.normal(loc=1,scale=2,size=(2,3))
print(x)


#Normal distribution
sns.displot(ran.normal(size=1000,loc=10,scale=0.1), kind="kde")

# plt.show()

#Binomial DIstribution

x=ran.binomial(n=10,p=0.5,size=10)
print(x)

sns.displot(ran.binomial(n=10,p=0.5,size=1000))
# plt.show()

# to find the difference between normal and binomial distribution
data = {
    "normal":ran.normal(loc=50,size=1000,scale=5),
    "binomial":ran.binomial(n=100,p=0.5,size=1000)
}
sns.displot(data,kind="kde")
plt.show()

