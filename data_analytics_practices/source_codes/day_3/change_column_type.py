import pandas as pd

path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_3\output.csv"
df = pd.read_csv(path_file, header = 0)

df.drop(df[["blue.1", "green.1", "red.1", "colors"]], axis = 1, inplace = True)
df = df.rename(columns={"colors.1": "color"})

df[["blue", "green", "red"]] = df[["blue", "green", "red"]].astype(int)

df.to_csv(path_file, index = False)

sum_of = df[["green", "blue", "red"]].sum()
print(sum_of, df)