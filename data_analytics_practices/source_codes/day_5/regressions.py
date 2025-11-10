import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_5\output.csv"
df = pd.read_csv(path, header = 0)

sns.regplot(x = "sales", y = "price", data = df)
plt.show()