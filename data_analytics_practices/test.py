import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "numbers": [0, 1, 2, 4, 6, 2, 76, 55, 33, 2, 33, 334, 22, 62, 12]
})

mean = df["numbers"].mean()
standard_deviation = df["numbers"].std()

print(f"this is the mean: {mean}, and this is the standard deviation: {standard_deviation}")
