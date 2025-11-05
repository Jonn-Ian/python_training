```python
################################################################################     CATEGORICAL VAR TO QUANTITATIVE VAR SECTION    ##########
#######################################################################
```
# One-hot

    # .get_dummies()

        get_dummies does is to get the values of how many the values occurs on the column, for example is we have 25 enteries in column genders, and the gender have a values of female and males.

        what we want is to separate the value female and male value in genders, so we can easily get the summaries how many female and how many males in gender

            ``` python

            # select the column that we want to apply the One-hot
            dummies = pd.get_dummies(df["colors.1"])

            # Merge the new dummy columns into the original DataFrame
            df = pd.concat([df, dummies], axis=1)

            # Save the updated DataFrame
            df.to_csv(path_file, index=False)
            ```