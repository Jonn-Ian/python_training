import pandas as pd
import numpy as np

path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_2\output.csv"

df = pd.read_csv(path, header = 0)

bins = np.linspace(min(df["length"]), max(df["length"]), 4)
group = ["low", "med", "high"]
df["place_holder"] = pd.cut(df["length"], bins=bins, labels = group, include_lowest = True)

miu = df["length"].sum() / df["length"].count()
theta = df["length"].std()
min_max = (df["length"] - df["length"].min()) / ["length"].min()

print(min_max)
