import pandas as pd
import json

# load files
path_file = r"E:\Git\my_repos\python_training\python_training\Arima Forecasting\codes\assets\output.csv"
json_file = r"E:\Git\my_repos\python_training\python_training\Arima Forecasting\codes\dictionary\dict.json"

with open(json_file, "r") as file:
    data = json.load(file)
df = pd.read_csv(path_file, header=0)

# month conversion
df["month"] = df["month"].astype("Int64").astype(str)
dict_months = data["months"]
df["month"] = df["month"].replace(dict_months)

# remove duplicates
df = df.drop_duplicates(subset=["year", "month", "products", "country"])

# remove rows if 2+ of the core columns are missing
df = df.drop(
    df[
        (df[["revenue", "sales"]].isna().all(axis=1)) |
        (df[["revenue", "price"]].isna().all(axis=1)) |
        (df[["sales", "price"]].isna().all(axis=1)) |
        (df[["sales", "price", "revenue"]].isna().all(axis=1))  # all three missing
    ].index
)

# normalize discounts to decimals
if df["discounts"].max() > 1:
    df["discounts"] = df["discounts"] / 100

# iterative filling with progress check
while True:
    print(df[["price", "sales", "revenue", "discounts"]].isna().sum())
    before = df[["price", "sales", "revenue", "discounts"]].isna().sum().sum()

    # fill price
    df.loc[df["price"].isna() & df["revenue"].notna() & df["sales"].notna(),
           "price"] = df["revenue"] / (df["sales"] * (1 - df["discounts"].fillna(0)))

    # fill sales
    df.loc[df["sales"].isna() & df["revenue"].notna() & df["price"].notna(),
           "sales"] = df["revenue"] / (df["price"] * (1 - df["discounts"].fillna(0)))

    # fill revenue
    df.loc[df["revenue"].isna() & df["sales"].notna() & df["price"].notna(),
           "revenue"] = df["sales"] * df["price"] * (1 - df["discounts"].fillna(0))

    # fill discounts
    df.loc[df["discounts"].isna() & df["revenue"].notna() & df["sales"].notna() & df["price"].notna(),
           "discounts"] = 1 - (df["revenue"] / (df["sales"] * df["price"]))
    df.loc[df["discounts"].isna(), "discounts"] = 0  # fallback

    after = df[["price", "sales", "revenue", "discounts"]].isna().sum().sum()
    if after == before:  # no progress → break
        break

# final check
print(df[["price", "sales", "revenue", "discounts"]].isna().sum())
print(df)

finished_file = r"E:\Git\my_repos\python_training\python_training\Arima Forecasting\codes\assets\output\cleansed.csv"

df.to_csv(finished_file, index = False)
print(f"the file has been saved into: {finished_file}")