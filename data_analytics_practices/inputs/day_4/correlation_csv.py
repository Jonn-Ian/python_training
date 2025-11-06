import pandas as pd
import numpy as np
import random

df = pd.DataFrame({
    "study_hours": np.random.normal(loc = 5, scale = 2, size = 100),
    "sleep_hours": np.random.normal(loc = 7, scale = 3, size = 100),
    "exam_score": np.random.normal(loc = 80, scale = 20, size = 100)
})
path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\correlation.csv"

df.to_csv(path)