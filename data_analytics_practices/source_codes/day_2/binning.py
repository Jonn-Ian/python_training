import pandas as pd
import numpy as np

file_path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_2\output.csv"
df = pd.read_csv(file_path, header = 0) # 0 means there's a head name which is the first row


# this codes identify which is high and which is low in num and 
# category it by 3.
binning = np.linspace(min(df["length"]), max(df["length"]), 4) #4 is to make a post to make a 3
# just imagine 4 is to create 4 fences to make 3 spaces
# |space|space|space|, | = 4, spaces = 3

label = ["low", "med", "high"]

df["place_holder"] = pd.cut(df["length"], bins=binning, labels=label, include_lowest=True)

print(df)