

# Statistical
this is where you can find or print the status of the column or the row value in total.

```python
###############################################################################################   MEAN SECTION    ############################
#######################################################################
```

# mean = df["normalized_losses"].mean()
with this line, we can see the average of the column value

``` python
mean = df["sales"].mean.() # this is for singular
print(mean)

mean = df[["sales", "price"]].mean() # this is for multiple
print(mean) # simply print the output
```

```python
#######################################################################################   MIN-MAX NORMALIZATION SECTION    ###################
#######################################################################
```

# Formula to get the max normalization
    max value formula is. new_val = old_val/max_old_val
    in pandas, this is how you do it.

    ``` python

    df["length"] = df["length"]/df["width"].max()

    ```

# Formula to get the min-max val
    as for minimum val. new_val = (old_val - min_val)/(max_old_val - min_old_val)

    ``` python
    # "placeholder" can be change to the same column or column you want to change tp
    df["placeholder"] = (df["length"] - df["length"].min()) / (df["length"].max() - df["length"].min())
    ```
        what this code simply does is, the first line where length - min length is to subtract all the length using the min length.
        the second one is to subtract the min length to the max length.
        then lastly, divide the value that we got from 1st formula and the 2nd fomurla.

# Formula for standard zero
    new_val = (original_val - miu)/standard deviation

    ``` python
    df["placeholder"] = (df["length"] - df["length"].mean())/df["length"].std()
    ```
