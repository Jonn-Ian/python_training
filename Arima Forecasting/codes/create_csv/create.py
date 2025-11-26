import pandas as pd
import numpy as np
import random

# Path to save the CSV
path = r"E:\Git\my_repos\python_training\python_training\Arima Forecasting\codes\assets\output.csv"

# Sample values for categorical columns
products = ["Widget A", "Widget B", "Widget C", "Gadget X", "Gadget Y"]
countries = ["USA", "UK", "Germany", "India", "Philippines", "Brazil"]

# Generate 1000 rows
n = 1000
df = pd.DataFrame({
    "year": np.random.choice([2022, 2023, 2024, 2025, None], size=n, p=[0.25,0.25,0.25,0.2,0.05]),
    "month": np.random.choice(list(range(1,13)) + [None], size=n),
    "products": np.random.choice(products + [None], size=n),
    "price": np.random.choice([10, 20, 30, 50, 100, None], size=n),
    "discounts": np.random.choice([0, 5, 10, 15, None], size=n),
    "sales": np.random.choice([1, 5, 10, 20, 50, None], size=n),
    "revenue": np.random.choice([100, 200, 500, 1000, None], size=n),
    "country": np.random.choice(countries + [None], size=n)
})

# Introduce duplicates by appending some rows again
df = pd.concat([df, df.sample(50, random_state=42)], ignore_index=True)

# Save to CSV
df.to_csv(path, index=False)
print(f"the file has been saved to: {path}")