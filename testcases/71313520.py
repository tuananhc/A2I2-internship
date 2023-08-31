```python
import pandas as pd

def replace_duplicate_ids(df):
    df['New_ID'] = df.groupby('ID')['ALT_ID'].transform('first')
    df.loc[df['New_ID'].isna(), 'New_ID'] = df['ID']
    df.drop_duplicates(subset='ID', keep='last', inplace=True)
    df.rename(columns={'New_ID': 'ID'}, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.drop(columns=['ALT_ID'], inplace=True)
    return df

class MyFuncTestCase(unittest.TestCase):
    def test_replace_duplicate_ids(self):
        df = pd.DataFrame({
            'ID': [1, 1, 2, 3, 3],
            'Name': ['Jack', 'James', 'Joe', 'Jim', 'Jen'],
            'ALT_ID': [111, 222, 333, 444, 555]
        })
        expected_df = pd.DataFrame({
            'ID': [1, 222, 2, 3, 555],
            'Name': ['Jack', 'James', 'Joe', 'Jim', 'Jen']
        })
        result_df = replace_duplicate_ids(df)
        self.assertTrue(result_df.equals(expected_df))

unittest.main(argv=[''], exit=False)
```