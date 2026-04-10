import pandas as pd

# DataFrames

data ={
    "calories":[420, 380, 390],
    "duration":[50, 40, 45],
    "day":["day1", "day2", "day3"]
}
myvar = pd.DataFrame(data)
# print()
# print(myvar)
# print(myvar.loc[[0,1]])

df=pd.DataFrame(data,index=["1", "2", "3"])
# print()
# print(df)
# print(df.loc['day2'])
df.to_csv("CSV3.csv")

# reading cvs files
df = pd.read_csv("CSV3.csv")
print(df.to_string())

# print(pd.options.display.max_rows)
# pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows)
df.to_json("CVS3.json")
df =pd.read_json("CVS3.json")
print(df.to_string())


