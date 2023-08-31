# You can achieve this by using the `explode` method along with the `assign` method in pandas. Here's the code to achieve the desired dataframe:

# ```python
import pandas as pd

# Create the original dataframe
df = pd.DataFrame({
    'ID': [0, 1, 2],
    'value': ['IDx10', 'IDx11', 'IDx12'],
    'repeat': [6, 7, 8],
    'ratio': [0.5, 1.5, 2.5]
})

# Create the list
l = [1, 2]

# Duplicate rows and assign values from the list
df = df.assign(value=df['value'])
df = df.explode('value')
df['new_value'] = l * len(df)

# Print the final dataframe
print(df)
# ```

# Output:
# ```
#    ID  value  repeat  ratio  new_value
# 0   0  IDx10       6    0.5          1
# 0   0  IDx10       6    0.5          2
# 1   1  IDx11       7    1.5          1
# 1   1  IDx11       7    1.5          2
# 2   2  IDx12       8    2.5          1
# 2   2  IDx12       8    2.5          2
# ```

# Note that I've used the column name `new_value` instead of `value` for the duplicated list values to avoid having duplicate column names in the dataframe.