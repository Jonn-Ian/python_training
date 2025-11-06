```python
############################################################################################     Data Visualization     ######################
#######################################################################
```

# heatmap()
    it highlights the highest, the dimmer the color, the higher the fader the color, the lower.

    example codes:

        ``` python

        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt

        path_file = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\outoput.csv"
        df = pd.read_csv(path_file, header = 0)

        group_by = df[["drive_wheels", "body_style", "price"]]

        grouped = df.groupby(["drive_wheels", "body_style"], as_index = False).mean()
        pivoted_table = grouped.pivot(columns = "drive_wheels", index = "body_style")

        plt.pcolor(pivoted_table, cmap="RdBu")
        plt.title("Heatmap")
        plt.xlabel("drive wheels")
        plt.ylabel("body style")
        plt.show()
        
        ```

# correlation
    this plot shows the relation between datas, if the line goes down it means negative if it is upward it's positive, if flat, no relation at all.

    - if the datas are spread out not close to the line or band, it means that the relation is weak, that it almost like no relation at all, or probably there's a variables

    - if the datas are close to the lines or trends, it means that they follow the trends and they also relates to each other, even if the datas below or above the line or bands.

    python example codes:

        ``` python
        import pandas as pd
        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt

        path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_4\correlation.csv"
        df = pd.read_csv(path, header = 0)

        correlation = sns.regplot(x = "sleep_hours", y = "exam_score", data = df)
        plt.ylim(0, )
        plt.show()
        ```
# pearson 

    Correlation coefficient:

        - if the value close to 1, it means it's a positive
        - if the value close to -1, it means it's a negative
        - if the value is 0, no relationship

    P - value:
        - p-value < 0.001 Strong certainty result
        - p-value < 0.05 moderate certainty
        - p-value < 0.1 weak certainty
        - p-value > 0.1 no certainty

    example python codes:

    ``` python
        import pandas as pd
        from scipy import stats

        # Load the data
        path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_2\output.csv"
        df = pd.read_csv(path)

        # Calculate Pearson correlation coefficient and p-value
        pearson_coef, p_value = stats.pearsonr(df["length"], df["width"])

        # Display results
        print(f"Pearson Correlation Coefficient: {pearson_coef:.3f}")
        print(f"P-value: {p_value:.3f}")
    ```