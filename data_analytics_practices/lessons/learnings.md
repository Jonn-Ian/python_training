```python
########################################################################################   descriptive statistics methods    #################
#######################################################################
```

``` python

mean(df[""])    df[""].mean() #both are the same

min() # for minimum, to show the lowest or can be used to formula
max() # for the maximum, to show the highest
mean() # to get the average
std() # to get the standard deviation
sum() # to get the summation
count() # to count, excluding no values
value_counts()# to count but indicate which value inside the parethesis
len() # can be use to count also but includes no values
median() # return middle value
mode() # returns the most repeated values
var() # 
describe() # gives the whole details of the pinpointed
quantile() # shows the percentage of the picked percentage

```

# quantile()

    ``` python
    df["length"].quantile(0.2)
    df["ID"].var()
    ```

# value_counts()
    ``` python
    counters = df["age"].value_counts()
    ```

```python
####################################################################################################   CRUD    ###############################
#######################################################################
```
``` python

# for READ
    pd.read_csv() #for csv
    pd.read_sql() #for sql
    pd.read_json() #for json
    pd.read_excel() #for excel but use xlwings package for xlsx or xlsm

# for UPDATE
    to_csv() # for csv
    to_sql() # for sql
    to_json() # for json
    to_excel() # for excel

    df = df.rename(columns={"old_name": "new_name"}) # rename column names


# for DELETE
    #axis = "1" is column, "0" is row. 
    # "inplace = True" means change it directly from the file
    df.drop(df["column_name"], axis = 1, inplace= True)
```


