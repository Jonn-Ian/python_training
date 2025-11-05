import pandas as pd
import random

path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_2\output.csv"
df = pd.read_csv(path_file)

color_choices = ["red", "blue", "green"]
arr = [random.choice(color_choices) for _ in range(len(df["ID"]))]

df["colors"] = arr

save_to = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_3\output.csv"
df.to_csv(save_to, index=False)

print(f"The file has been saved to: {save_to}")