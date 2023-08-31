# To achieve the desired result, you can use the `any` function along with the `axis` parameter in `np.where`. Here's how you can modify your code to get the expected output:

# ``` python
import pandas as pd
import numpy as np

data = {"Close": [0.1, 0.2], "M": [0.2, 0.1], "N": [0.3, 0.6], "O": [0.4, 0.1], "P": [0.5, 0.0]}
df = pd.DataFrame(data=data)
print(df)
Colslist = ['M','N','O','P']

df["Q"] = np.where((df[Colslist] >= (df["Close"].values.reshape(-1, 1) + 0.3)).any(axis=1), 1, 0)
print(df["Q"])
# ```

# Explanation:
# - `df["Close"].values.reshape(-1, 1)` converts the "Close" column into a 2D array with the same number of rows as the dataframe, allowing for element-wise addition with the Colslist columns.
# - `df[Colslist] >= (df["Close"].values.reshape(-1, 1) + 0.3)` produces a boolean dataframe where each value is True if the corresponding value in Colslist is greater than or equal to the corresponding value in "Close" plus 0.3.
# - `any(axis=1)` checks if any value in each row of the boolean dataframe is True, returning a boolean Series indicating whether each row satisfies the condition.
# - `np.where(..., 1, 0)` assigns 1 to rows where the condition is True and 0 to rows where it is False.

# The resulting dataframe will have the "Q" column with the values 1 in both rows since both rows have at least one value greater than or equal to "Close" + 0.3.