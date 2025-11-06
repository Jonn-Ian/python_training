import pandas as pd

read_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\outoput.csv"

df = pd.read_csv(read_file, header = 0)

df_test = df[["drive_wheels", "body_style", "price"]]
df_group = df_test.groupby(["drive_wheels", "body_style"], as_index = False).mean()

print(df_group)