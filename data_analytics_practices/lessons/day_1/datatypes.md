
```python
###############################################################################################   DESCRIBE SECTION   #########################
#######################################################################
```

# .describe()
    declare the path and load the file first to check the data types

        ``` python

        import pandas as pd
        import glob

        folder_path = r"something/something/something"

        df = pd.read_csv(folder_path, header = 1)
        print("\n===========================")
        print("this is describe")
        print("\n===========================")
        print(df.describe())#this is the example of describe which count, min, max, standard deviation, etch...
        print("\n===========================")

        #this code is for specific describe
        print(df["name"].describe())#change the name to the header

        ```

```python
###############################################################################################   INFO SECTION    #########################
#######################################################################
```

# info()
    df.info() does is to show what variable type is the header is
    for example, num = 1, it'll print the num is int64

        ``` python

        print(info())

        #example output:

        #   Column             Non-Null Count  Dtype
        ---  ------             --------------  -----
        0   symboling          205 non-null    int64
        1   normalized_losses  205 non-null    object
        2   make               205 non-null    object
        3   fuel-type          205 non-null    object
        4   aspiration         205 non-null    object
        5   num-of-doors       205 non-null    object
        6   body-style         205 non-null    object
        7   drive-wheels       205 non-null    object
        8   engine-location    205 non-null    object
        9   wheel-base         205 non-null    float64
        10  length             205 non-null    float64
        11  width              205 non-null    float64
        12  height             205 non-null    float64
        13  curb-weight        205 non-null    int64
        14  engine-type        205 non-null    object
        15  num-of-cylinders   205 non-null    object
        16  engine-size        205 non-null    int64
        17  fuel-system        205 non-null    object
        18  bore               205 non-null    object
        19  stroke             205 non-null    object
        20  compression-ratio  205 non-null    float64
        21  horsepower         205 non-null    object
        22  peak-rpm           205 non-null    object
        23  city-mpg           205 non-null    int64
        24  highway-mpg        205 non-null    int64
        25  price              205 non-null    object
        dtypes: float64(5), int64(5), object(16)

        # you can also do this to know the column info
        show_info = df["name"].info()
        print(show_info)

        #or this for multiple
        df[["column1", "column2", "column3"]].info()
        ```

```python
###############################################################################################   DTYPES SECTION    #########################
#######################################################################
```

# .dtypes()

    df.dtypes() is the same as df.info()
    but it only print what variable is it like, object, int, float etch

        ``` python

        print(df.types())

        ```

```python
########################################################################################   CORRECTING DATA TYPES SECTION    ##################
#######################################################################
```

# df[""].astype("")
    you can replace value of the column name inside the df[""] and change it into the value that you want by using .astype("").

    for example bool to int simply do this.

        ``` python

        df["0/1"].astype("int") # the boolean will turn to int
        df[["price", "sales"]].astype("int") # to change multiple types to one
        df[["price", "sales"]].astype({"price": int, "sales": str}) # to change multiple types to multiple types

        ```


```python
################################################################################################   BONUS SECTION    ##########################
#######################################################################
```

# bonus

    if you want to choose multiples variables, then you must use double brackets [[]], if not you're just calling one variable then use only one bracket[]

        ``` python
        df[["name", "length"]].describe() # change the name and length to your own header's name

        ```