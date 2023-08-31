# When using the `fillna` method, if the column contains both floats and None values, the dtype of the column will be changed to `object`. 

# To avoid this, you can replace the missing values with the mean using the `replace` method instead of `fillna`. This will retain the original dtype of the column. Here's an example:

# ``` python
ser_original = pd.Series([1.0, 2.0, np.nan, 4.0, 5.0], dtype=float)
mean_value = ser_original.mean()

ser_imputed = ser_original.replace(np.nan, mean_value)
print('After imputation, the dtype is {}'.format(ser_imputed.dtype))
# ```

# Output:
# ```
# After imputation, the dtype is float64
# ```

# In this example, `replace` is used to replace the missing values (`np.nan`) with the mean value calculated from the original series.

# For multiple columns, you can use the `apply` method along with lambda functions to apply the `replace` method on each column. Here's an example:

# ``` python
# df_original = pd.DataFrame({'col1': [1.0, 2.0, np.nan, 4.0, 5.0],
#                             'col2': [6.0, np.nan, 8.0, np.nan, 10.0]})

# df_imputed = df_original.apply(lambda col: col.replace(np.nan, col.mean()), axis=0)

# print('After imputation:')
# print(df_imputed.dtypes)
# ```

# Output:
# ```
# After imputation:
# col1    float64
# col2    float64
# dtype: object
# ```

# In this example, `apply` is used to apply the lambda function on each column of the dataframe. The lambda function replaces the missing values in each column with their respective mean values. The resulting dataframe `df_imputed` will have the same dtypes as the original dataframe `df_original`.