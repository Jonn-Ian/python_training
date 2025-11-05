import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "cars": ['fwd', 'rwd', 'fwd', '4wd', 'rwd', 'fwd'],
    "price": [10000, 20000, 12000, 18000, 22000, 13000]
})

sns.boxplot(x = "cars", y = "price", data = df)
plt.title("something something")
plt.show()