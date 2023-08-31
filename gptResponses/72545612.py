# You can use the `applymap` method to apply a function to each element in the dataframe and add the string prefix to non-missing values. Here's how you can do it:

# ``` python
df.applymap(lambda x: '+' + str(x) if pd.notna(x) else '')
# ```

# The `applymap` method applies the lambda function to each element in the dataframe. The lambda function checks if the element is not missing using `pd.notna(x)`, and if so, it adds the string prefix '+' to it using `'+'.join(x.split())`. If the element is missing, an empty string is returned.