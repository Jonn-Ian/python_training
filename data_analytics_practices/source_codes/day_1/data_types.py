import pandas as pd

file_path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_1\automobile.csv"

df = pd.read_csv(file_path)
print("this is describe")
print(df.describe())
print("\n===========================")

print("\n===========================")
print("this is info")
print("\n===========================")
print(df.info())
print("\n===========================")

print("\n===========================")
print("this is dtypes")
print("\n===========================")
print(df.dtypes)
print("\n===========================")


#for specific describe
print("\n===========================")
print(df["symboling"].describe())
print("\n===========================")

for i in range(len(df.columns)):
    print(df.columns[i])
