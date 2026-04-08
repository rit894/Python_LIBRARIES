from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(df=1,size =1000),kind='kde')
plt.show()

sns.displot(random.rayleigh(scale=0.9,size=1000),kind = 'kde')
plt.show()

data = {
    'chisquare': random.chisquare(df=1, size=1000),
    'rayleigh':random.rayleigh(scale=0.9,size=1000)
}
sns.displot(data,kind='kde')
plt.show()

