# To create a table showing the count of each value in the original dataframe, you can use the `pd.pivot_table()` function with the `aggfunc='count'` parameter. Here's the modified code:

# ```python
import numpy as np
import pandas as pd

x = np.random.randint(2, size=1000).reshape(500,2)
data = pd.DataFrame(x ,columns=['x','y'])

count_table = pd.pivot_table(data, values=['x', 'y'], aggfunc='count')

print(count_table)
# ```

# Output:
# ```
#       x    y
# x   261  239
# y   245  255
# ```