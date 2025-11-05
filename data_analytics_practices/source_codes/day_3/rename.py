import pandas as pd

path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_3\output.csv"

df = pd.read_csv(path_file, header = 0)

df = df.rename(columns = {"ID": "colors"})

df["colors"].astype(str)

df.to_csv(path_file, index = False)
print(df)