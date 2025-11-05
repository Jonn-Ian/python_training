import pandas as pd

file_path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\inputs\automobile\imports-85.data"

# Custom headers
file_headers = ["symboling", "normalized_losses", "make", "fuel-type",
                "aspiration", "num-of-doors", "body-style", "drive-wheels",
                "engine-location", "wheel-base", "length", "width", "height",
                "curb-weight", "engine-type", "num-of-cylinders", "engine-size",
                "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
                "peak-rpm", "city-mpg", "highway-mpg", "price"]

# Read file without header row
df = pd.read_csv(file_path, header=None)

#to add a header
df.columns = file_headers

# Save to CSV
save_path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs"
output_file = save_path + r"\automobile.csv"
df.to_csv(output_file, index=False)
