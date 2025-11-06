import pandas as pd

df = pd.DataFrame({
    "drive_wheels": [
        "FWD", "RWD", "AWD", "FWD", "RWD", "AWD", "FWD", "RWD", "AWD", "FWD",
        "RWD", "AWD", "FWD", "RWD", "AWD", "FWD", "RWD", "AWD", "FWD", "RWD",
        "AWD", "FWD", "RWD", "AWD", "FWD", "RWD", "AWD", "FWD", "RWD", "AWD"
    ],
    "body_style": [
        "Sedan", "Coupe", "SUV", "Hatchback", "Convertible", "Wagon", "Sedan", "Coupe", "SUV", "Hatchback",
        "Convertible", "Wagon", "Sedan", "Coupe", "SUV", "Hatchback", "Convertible", "Wagon", "Sedan", "Coupe",
        "SUV", "Hatchback", "Convertible", "Wagon", "Sedan", "Coupe", "SUV", "Hatchback", "Convertible", "Wagon"
    ],
    "price": [
        22500, 28000, 35000, 18700, 32500, 27300, 21800, 29400, 36200, 19100,
        33000, 28000, 23000, 30500, 37800, 20000, 34200, 29100, 24300, 31700,
        38500, 20800, 35000, 30400, 25600, 32900, 39200, 21500, 36300, 31600
    ]
})

save_to = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\correlation.csv"

df.to_csv(save_to, index = False)
print(f"the data has been saved into: {save_to}")