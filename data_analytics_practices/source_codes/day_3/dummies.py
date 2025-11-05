import pandas as pd

path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_3\output.csv"
df = pd.read_csv(path_file, header=0)

# Apply one-hot encoding to 'colors.1'
dummies = pd.get_dummies(df["colors.1"])

# Merge the new dummy columns into the original DataFrame
df = pd.concat([df, dummies], axis=1)

# Save the updated DataFrame
df.to_csv(path_file, index=False)

# Print the updated DataFrame
print(df)