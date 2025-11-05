```python
############################################################################################     DESCRIPTIVE STATISICS    ####################
#######################################################################
```

# value_counts()
    similar to counts but this, specifically counts the data that you appoint, for example:

        ``` python
        # this counters the every colors
        counters = value_counts(df["colors"])

        # output:
        # pink: 34
        # white: 33
        # black: 50
        ```

# Box Plots
    it shows the visualization of the datas, this is a seaborn library

    ``` python
    sns.boxplot(x = "drives-wheel", y = "price", data = df)
    ```