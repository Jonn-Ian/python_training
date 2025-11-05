```python
###############################################################################################     BINNING SECTION    #######################
#######################################################################
```
# INSTRUCTIONS
    binning uses a numpy, so install the numpy

# Binning
    binning is a method where you categorize or group the column or rows into a one thing for it to be more easier to understand or accurate. one of the example is:
    
     - easy, medium, and hard level.
     - (15k - 19k), (20k - 25k), (26k - 30k)

     the code for binning is:

``` python
bins = np.linspace(min(df["price"]), max(df["price"]), 4) # now this group to low and high

group_names = ["low", "med", "high"]

df["price"] =pd.cut(df["price"], bins, labels = group_names, include_lowest = True)

```
