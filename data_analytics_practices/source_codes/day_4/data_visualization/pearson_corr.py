import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats  # ✅ This line is missing in your code

# Load the data
path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_2\output.csv"
df = pd.read_csv(path)

# Calculate Pearson correlation coefficient and p-value
pearson_coef, p_value = stats.pearsonr(df["length"], df["width"])

# Display results
print(f"Pearson Correlation Coefficient: {pearson_coef:.3f}")
print(f"P-value: {p_value:.3f}")