import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\outoput.csv"
df = pd.read_csv(path_file, header=0)

pivot_df = df.pivot_table(values="price", index="body_style", columns="drive_wheels", aggfunc="mean")

# change the size by width and height
# 10 for widthm 6 for height
plt.figure(figsize=(10, 6))

# cmap is a color, cbar is the legend 
sns.heatmap(pivot_df, cmap="RdBu", annot=True, cbar=True)

plt.title("Average Price by Body Style and Drive Wheels")
plt.xlabel("Drive Wheels")
plt.ylabel("Body Style")
plt.show()