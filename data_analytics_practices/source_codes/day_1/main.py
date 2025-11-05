import pandas as pd
import numpy as np

# Load the CSV file
path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_2\output.csv"
df = pd.read_csv(path_file, header=1)

# Remove duplicates
df = df.drop_duplicates()

# Create bins and labels
bins = np.linspace(df["length"].min(), df["length"].max(), 4)
labels = ["low", "medium", "high"]

# Categorize 'length' into bins
df["length_category"] = pd.cut(df["length"], bins=bins, labels=labels, include_lowest=True)

# Display the DataFrame
print(df)