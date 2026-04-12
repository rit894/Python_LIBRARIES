import pandas as pd
df = pd.read_csv("D:\Python_LIBRARIES\Pandas\CSVfiles\CD1.csv")
# df1 = pd.read_csv("D:\Python_LIBRARIES\Pandas\CSVfiles\workout_data.csv")
# df1.dropna(inplace=True)
# print(df.to_string())
# print(df1.to_string())

new_df=df.fillna({"Calories":130})
# print(new_df.to_string())
# print(df.to_string())
x = df["Calories"].mean()
df1 = df.fillna({"Calories":x})

print(df1.to_string())

