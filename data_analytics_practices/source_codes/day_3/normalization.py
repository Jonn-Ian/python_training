import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_3\output.csv"
df = pd.read_csv(path_file, header = 0)

df["place_holder"] = df["length"]/max(df["length"]) # normalize
counter = df["color"].value_counts()

print(df, counter)