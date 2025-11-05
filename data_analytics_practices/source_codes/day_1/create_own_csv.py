import pandas as pd
import numpy as np

j = 150
k = 354
l = 0

ids = []
length = []
width = []
place_holder = []

for i in range(25):
    l = l + 1
    j = j + 2
    k = k + 3

    ids.append(i + 1)
    length.append(j)
    width.append(k)
    place_holder.append("Nan")

df = pd.DataFrame({
    "ID": ids,
    "length": length,
    "width": width,
    "place_holder": place_holder
})

save_to = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_2\output.csv"
df.to_csv(save_to, index = False)
print(f"file has been saved to {save_to}")