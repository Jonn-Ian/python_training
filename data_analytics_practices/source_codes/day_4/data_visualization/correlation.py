import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\correlation.csv"
df = pd.read_csv(path, header = 0)

correlation = sns.regplot(x = "sleep_hours", y = "exam_score", data = df)
plt.ylim(0, )
plt.show()