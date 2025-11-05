import pandas as pd
import numpy as np

file_path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\inputs\day_1\automobile\imports-85.data"
df = pd.read_csv(file_path, header = None)

# this codes identify which is high and which is low in num and 
# category it by 3.
binning = np.linspace(min(df[]), max(num), 4) #4 is to make a post to make a 3
# just imagine 4 is to create 4 fences to make 3 spaces
# |space|space|space|, | = 4, spaces = 3

label = ["low", "med", "high"]

group = pd.cut(num, bins=binning, labels=label, include_lowest=True)

print(group)