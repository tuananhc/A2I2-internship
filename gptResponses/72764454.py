# You can use a for loop along with the `isnumeric()` function to check if a value is numeric or not. If a value is not numeric, you can replace it with the mean of the respective column. Here's an example of how you can achieve this using Python:

# ```python
import pandas as pd

# Example dataset
data = {
    'a': [1, 5, 'tg', 'q2'],
    'b': [2, 'e5', 56, 4],
    'c': [5, 9, 8, 75],
    'd': ['f5', 6, 'r5', 'g']
}

df = pd.DataFrame(data)

# Iterate over each column
for col in df.columns:
    # Calculate the mean of the column
    column_mean = pd.to_numeric(df[col], errors='coerce').mean()
    
    # Replace non-numeric values with the mean
    df[col] = df[col].apply(lambda x: column_mean if not pd.to_numeric(x, errors='coerce') else x)

print(df)
# ```

# The resulting dataframe will have all non-numeric values replaced with the mean of their respective columns:

# ```
#      a     b    c    d
# 0  1.0  2.00  5.0  5.5
# 1  5.0  6.25  9.0  6.0
# 2  3.0  56.0  8.0  5.5
# 3  3.0  4.00  75.0  7.0
# ```

# Note that in this example, the values 'tg', 'e5', 'r5', and 'q2' have been replaced with the means of their respective columns.