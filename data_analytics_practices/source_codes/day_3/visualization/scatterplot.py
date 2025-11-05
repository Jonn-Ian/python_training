import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_3\output.csv"
df = pd.read_csv(path_file, header = 0)

bins = np.linspace(df["length"].min(), df["length"].max(), 3)
group_length = ["short", "tall"]

df["place_holder"] = pd.cut(df["length"], bins = bins, labels = group_length, include_lowest=True)

sns.scatterplot(x = df["length"], y = df["width"], data = df)

plt.title("short vs tall")
plt.xlabel("length") and plt.ylabel("width")
plt.show()