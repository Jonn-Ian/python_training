```python
#################################################################################################   READ SECTION    ##########################
#######################################################################
```

### **Day 1: Read, Write, and Save on CSV using pandas**

    to read the data from csv you must declare the path first of the file, you can do this by doing this

        ```python
        # This is a simple Python program that declares the path of the file
        file_path = r"something/something/semething.csv"
        ```

# load the csv
    then to access the csv, you should load the file by doing this:

        ``` python
        #by doing this, you can already read the csv file and load it
        df = pd.read_csv(file_path)
        ```


# no header load from csv
    to load a csv without a header, you can do this by adding None attribute

        ``` python
        df = pd.read_csv(file_path, header = None) # you can also add a header by changing the None to a number value like 1
        ```


# then you can also make your own headers
    to make your own headers, create a lists of elements

        ``` python

        file_headers = ["symboling", "normalized_losses", "make", "fuel-type",
                        "aspiration", "num-of-doors", "body-style", "drive-wheels",
                        "engine-location", "wheel-base", "length", "width", "height",
                        "curb-weight", "engine-type", "num-of-cylinders", "engine-size",
                        "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
                        "peak-rpm", "city-mpg", "highway-mpg", "price"]

        ```

```python
###############################################################################################   UPDATE SECTION    ##########################
#######################################################################
```

# merge and update
    to merge the headers and csv

        ``` python
        df.columns = file_headers # to print all the columns, if you want to find all the names of the header

        for i in range(len(df.columns)):
            print(df.columns[i]) #to print it one by one
        ```

# Update
    for saving a csv you must you can use the same csv file or create a new file by declaring it to the path, for example:

        ``` python

        # declare the output path file with the name
        output_path = r"here/there/file.csv"# you can change the file name to anything just don't forget the extension

        df.csv_to(output_path)#csv_to() is the key word to save it to what file and what folder

        ```


# df.replace(missing_val, new_val)
    replace replacing the old value by a new value

        ``` python
        mean = df["sales"].mean() # create a mean by using the average of sales
        df["price"] = df["price"].replace(np.nan, mean) # replace no value with the value of mean

        print(mean) # show the mean
        ```


```python
###############################################################################################   DDELETE SECTION    #########################
#######################################################################
```

# Delete
    by using "df.dropna()" you can remove the entire row or columns
    one of the example of this is:

        ``` python
        #change the price to whatever name you want that exist in file csv
        df.drop(["price"], axis = 0, inplace = True) # 0 = row, 1 = column, and inplace = True means change it directly from the file

        # this is also one of the method to remove specific row or column
        df.drop(1, axis = 0, inplace = True)

        # or like this
        df.drop([0, 2, 4], axis = 1, inplace = True)# this is for multiple column that you want to remove, with axis = 1 I'm removing the whole column 

        df.dropna(subset = ["sales"], axis = 1, inplace = True) # by doing this, I can delete the row without a value or column specifically

        df.dropna(subset = [["sales", "price"]], axis = 0, inplace = True) # by doing this, I can remove multiple rows that don't have a value using multiple select

        ```
    there's a difference between "dropna" and "drop"
    "dropna" only removes the specific row or column that don't have a value

    while "drop" removes a column or row, with or without a value 


# df.drop_diplicates(subset = "")
    next is dropping the duplicates for more accurate data visualization, in data cleaning, duplicates is normal occurance, we can do this by doing this.

        ``` python

        df.drop_duplicates() # this removes the general duplicates
        df.drop_duplicates(subset = ["name"]) # this removes duplicates by specific column
        df.drop_duplicates(subset = ["name", "salary"]) # this removes duplicates by multiple selected columns

        ```


```python
################################################################################################   CREATE SECTION    #########################
#######################################################################
```


# bonus
    lastly the pandas can also read other files such as json, excel (but better to use xlwings package), etch...

    this is the examples of other formats

        ``` python

        # for reading
        pd.read_csv() #for csv
        pd.read_sql() #for sql
        pd.read_json() #for json
        pd.read_excel() #for excel but use xlwings package for xlsx or xlsm

        # for saving
        to_csv() # for csv
        to_sql() # for sql
        to_json() # for json
        to_excel() # for excel

        ```



``` python
#####################################################################################################################################################################################################################
```

