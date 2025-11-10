import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\correlation.csv"
df = pd.read_csv(path, header = 0)

group_by = df[["study_hours", "sleep_hours", "exam_score"]]
grouped = group_by.groupby(["study_hours", "sleep_hours", "exam_score"], as_index = False).mean()

pivot_table = grouped.pivot(index = "study_hours", columns = "sleep_hours")

sns.scatterplot(x = df["study_hours"], y = df["exam_score"], data = df)

pearson_coef, p_value = stats.pearsonr(df["study_hours"], df["sleep_hours"])

print(f"coef: {pearson_coef:.3f}")
print(f"p_val: {p_value:.3f}")
plt.show()

