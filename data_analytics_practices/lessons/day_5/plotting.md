```python
############################################################################################     LINEAR REGRESSION (EDA)     #################
#######################################################################
```

# Regression Plot Tutorial

    ``` python
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.regplot(x="", y="", data = df)
    plt.ylim(y, )
    ```

# simple linear regression
    1. the predictor (indepent variable) = "x"
    2. the target (dependent variable) = "y"

    example explanation:

        x = meter
        y = price
        
        z is will be the value of the car per meter
        z = intecept of x and y
        z = (x, y)
    
    to use the linear regression, we need to import the scipy first

    ``` python
        # to use the linear regression visualization
        from sklearn.linear_model import LinearRegression

        lm = LinearRegression()
    ```

    now we need to define the datas that we will be using.

    ``` python
        x = df[["highway-mpg"]]
        y = df["price"]

        # fit the model here
        lm.fit(x, y)

        # obtain the prediction using the method predict
        yhat = lm.predict(x) 
    ```


```python
###############################################################################################     RESIDUAL PLOT     ########################
#######################################################################
```

# residual plot
    residual plot shows the represents the error between the actuall value.

    the simple formula of it is like this:
    residual = actual value - predicted value

    if the plot is curve like, it means that the plot is not a linear

    example code:
    
        ``` python
            import seaborn as sns
            import pandas as pd
            import matplotlib.pyplot as plt

            path = r"" # path 
            df = pd.read(path, header = 0)
            sns.regplot(x = "price", y = "sales", data = df)
            sns.resigplot(x = "price", y = "sales", data = df)
            plt.show()
        ```

```python
############################################################################################     DISTRIBUTION PLOT     #######################
#######################################################################
```

# Distribution plot
    the distribution plot, count and show the two target like linear graph, this is useful for multiple values.

    ``` python
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    path = r"E:\Git\my_repos\python_training\python_training\data_analytics_practices\outputs\day_5\output.csv"
    df = pd.read_csv(path, header = 0)

    # Simulate predicted prices (90% of actual)
    Yhat = df["price"] * 0.9

    ax1 = sns.kdeplot(df["price"], color="r", label="Actual Price")
    sns.kdeplot(Yhat, color="b", label="Predicted Price", ax=ax1)

    plt.title("actual vs predicted price distribution")
    plt.legend()
    plt.show()

    ```

