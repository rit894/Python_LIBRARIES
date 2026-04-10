import pandas as pd

df = pd.read_csv("D:\\Python_LIBRARIES\\Pandas\\pandasTutorial\\CSVfiles\\CSV4.csv")
print(df.head(61))
print(df.tail(45))
print(df.info())