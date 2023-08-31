# Yes, you can achieve that by using the `exec` function to dynamically create variables with the sheet names. Here's how you can modify your loop:

# ```python
import pandas as pd

sheets = pd.read_excel('Data Series.xlsx',sheet_name=None)

for sheet, dataframe in sheets.items():
    exec(f"df_{sheet} = dataframe")

# ```

# This loop will create a separate dataframe variable for each sheet, with a name like `df_CPI`, `df_Sheet2`, etc., containing the corresponding dataframe from the `sheets` dictionary.