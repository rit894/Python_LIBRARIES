from numpy import random as r


# Data Distribution is a list of all possible values, and how often each value occurs.

# Such lists are important when working with statistics and data science.

# The random module offer methods that returns randomly generated data distributions.



x=r.choice([3,2,4,5],p=[0.1,0.5,0.2,0.2],size=(3,5))
print(x)