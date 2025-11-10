import pandas as pd
import numpy as np

np.random.seed(1)

# Generate base dataset
orders = pd.DataFrame({
    "order_id": range(1001, 1101),
    "customer_id": np.random.randint(1, 51, 100),
    "product": np.random.choice(["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"], 100),
    "quantity": np.random.randint(1, 5, 100),
    "price": np.round(np.random.uniform(100, 2000, 100), 2),
    "order_date": pd.date_range(start="2025-01-01", periods=100, freq="D")
})

# Add new columns
orders["name"] = np.random.choice(["Alice", "Bob", "Charlie", "Diana", "Ethan"], 100)
orders["sales"] = orders["quantity"] * orders["price"]
orders["stock_quantity"] = np.random.randint(10, 100, 100)
orders["rating"] = np.random.choice([1, 2, 3, 4, 5], 100)
orders["region"] = np.random.choice(["North", "South", "East", "West"], 100)

save_path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_5\output.csv"

orders.to_csv(save_path, index = False)
print(f"the datas been saved to: {save_path}")