```python
import pandas as pd
import unittest

def myFunc(df, values):
    new_rows = []
    for index, row in df.iterrows():
        for value in values:
            new_row = row.copy()
            new_row['value'] = value
            new_rows.append(new_row)
    return pd.concat(new_rows, ignore_index=True)

class TestMyFunc(unittest.TestCase):
    def test_myFunc(self):
        df = pd.DataFrame({
            'ID': [0, 1, 2],
            'value': ['IDx10', 'IDx11', 'IDx12'],
            'repeat': [6, 7, 8],
            'ratio': [0.5, 1.5, 2.5]
        })
        values = [1, 2]

        expected_df = pd.DataFrame({
            'ID': [0, 0, 1, 1, 2, 2],
            'value': ['IDx10', 'IDx10', 'IDx11', 'IDx11', 'IDx12', 'IDx12'],
            'repeat': [6, 6, 7, 7, 8, 8],
            'ratio': [0.5, 0.5, 1.5, 1.5, 2.5, 2.5],
            'new_value': [1, 2, 1, 2, 1, 2]
        })

        result = myFunc(df, values)
        self.assertTrue(result.equals(expected_df))

unittest.main(argv=[''], exit=False)
```