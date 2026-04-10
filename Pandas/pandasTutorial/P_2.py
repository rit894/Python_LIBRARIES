import pandas as pd

a=[1,2,3,4,5]
myvar =pd.Series(a)
# print(myvar)

# print(myvar[0]) # labels

# Creating Labels

myvar = pd.Series(a, index=["a", "b", "c", "d", "e"])
# print(myvar)

# print(myvar["e"])

# Key/value Objects as Series
calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}
myvar = pd.Series(calories)
# print(myvar)

# Selecting personlised keys in Series
my = pd.Series(calories, index=["day1", "day2"])
# print(my)

