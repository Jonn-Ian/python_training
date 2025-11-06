import pandas as pd

read_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\outoput.csv"

df = pd.read_csv(read_file, header = 0)

group_by = df[["drive_wheels", "body_style", "price"]]
grouped = group_by.groupby(["drive_wheels", "body_style"], as_index = False).mean()

df_pivot = grouped.pivot(index = "drive_wheels", columns = "body_style")

print(df_pivot)