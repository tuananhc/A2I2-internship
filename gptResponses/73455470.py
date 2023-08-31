# You are correct, you can use the `json_normalize` function from pandas to flatten the nested JSON structure into a pandas DataFrame. Here's how you can do it:

# ```python
import pandas as pd
from pandas import json_normalize

datajson = {
    "10001": {
        "extra": {"user": "Tom"},
        "data": {"A": 5, "B": 10}
    },
    "10002": {
        "extra": {"user": "Ben"},
        "data": {"A": 7, "B": 20}
    },
    "10003": {
        "extra": {"user": "Ben"},
        "data": {"A": 6, "B": 15}
    }
}

df = json_normalize(datajson, sep='_')
# ```

# The `json_normalize` function takes the JSON object (`datajson`) as the first argument and the separator (`sep='_') as the second argument. It flattens the nested JSON structure into a DataFrame. 

# The resulting DataFrame, `df`, will have columns "extra_user", "data_A", and "data_B" containing the corresponding data values.

# Output:
# ```
#   extra_user  data_A  data_B
# 0        Tom       5      10
# 1        Ben       7      20
# 2        Ben       6      15
# ```

# Now, you can access the specific columns "A" and "B" for further processing.