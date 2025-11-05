```python
#################################################################################################     MATPLOTLIB    ##########################
#######################################################################
```

# boxplot
    to use this library you must set an allias for this, for example:

        ``` python
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt

        # create an own datas
        df = pd.Dataframe({
            "price": [1000, 2000, 3000, 4000, 5000, 6000, 7000],
            "cars": ['fwd', 'rwd', 'fwd', '4wd', 'rwd', 'fwd']
        })
        
        # create a formula that shows the graph of price of cars
        plot_this = sns.boxplot(x = "price", y = "cars", data = df)

        # gives a title to the graph
        plt.title("give a title for your visualization here")

        # this shows the visualization that you did in the formula
        plt.show(plot_this) 
        ```

# scatterplot
    this show the graph of the scatter datas

    ``` python 
    df = pd.DataFrame({
        "color": ["pink", "yellow", "green"],
        "cars": ["ferrari", "toyota", "ford"],
        "price": [2000, 1000, 3000]
    })

    sns.scatterplot(x = "colors", y = "cars", data = df)
    plt.title("price of cars")
    plt.xlabel("colors")
    plt.ylabel("cars")
    plt.show()
    ```