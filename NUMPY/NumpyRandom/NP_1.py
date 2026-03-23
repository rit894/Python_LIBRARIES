from numpy import random as r

x= r.randint(100) # used to generate random number
print(x)

x= r.rand()
print(x) # used to generate random numbers between 0 and 1

x=r.randint(100,size=(3,5))# used to generate a random array
print(x)

x=r.rand(5,3)# used to generate an array with random float points
print(x)

x=r.choice([3,2,5,54,8]) #method allows you to generate a random value based on an array of values.
print(x)

x = r.choice([3, 5, 7, 9], size=(3, 5))
print(x)