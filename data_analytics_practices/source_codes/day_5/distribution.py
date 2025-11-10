import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_5\output.csv"
df = pd.read_csv(path, header = 0)

# Simulate predicted prices (90% of actual)
Yhat = df["price"] * 0.9

ax1 = sns.kdeplot(df["price"], color="r", label="Actual Price")
sns.kdeplot(Yhat, color="b", label="Predicted Price", ax=ax1)

plt.title("actual vs predicted price distribution")
plt.legend()
plt.show()
