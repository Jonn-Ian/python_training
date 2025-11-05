# df.sort_values(by = "name", ascending = True)
when dealing with data, sorting is the best for searching for a duplicates, to do that, this is the example code to sort the data by column or by or by value

``` python

df_sorted = df.sort_values(by = "age", ascending = True) # change the age to your own column name, with this, the data will be sorted by age

# for multiple sort
df_sorted = df.sort_values(by = ["name", "age"], ascending = [True, False]) # with this, the data will be sorted by name and age

```

``` python
#####################################################################################################################################################################################################################
```
