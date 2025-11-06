import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\outoput.csv"
df = pd.read_csv(path_file, header = 0)

group_by = df[["drive_wheels", "body_style", "price"]]

grouped = df.groupby(["drive_wheels", "body_style"], as_index = False).mean()
pivoted_table = grouped.pivot(columns = "drive_wheels", index = "body_style")

plt.pcolor(pivoted_table, cmap="RdBu")
plt.title("Heatmap")
plt.xlabel("drive wheels")
plt.ylabel("body style")
plt.show()