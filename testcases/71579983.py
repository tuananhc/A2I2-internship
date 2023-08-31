Here are some unit test cases for the 'myFunc' function:

```python
import unittest
import pandas as pd

def myFunc():
    sheets = pd.read_excel('Data Series.xlsx', sheet_name=None)
    for sheet, dataframe in sheets.items():
        globals()[f"df_{sheet}"] = dataframe

class MyFuncTestCase(unittest.TestCase):

    def test_sheet_names(self):
        myFunc()
        sheet_names = ['CPI', 'Sheet1', 'Sheet2', 'Sheet3'] # Assuming these are the sheet names in the Excel file
        for sheet_name in sheet_names:
            self.assertIn(f"df_{sheet_name}", globals())

    def test_dataframes(self):
        myFunc()
        df_CPI = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) # Sample expected dataframe for sheet 'CPI'
        self.assertTrue(df_CPI.equals(globals()["df_CPI"]))

if __name__ == '__main__':
    unittest.main()
```

In the first test case `test_sheet_names`, we check if the dataframes are assigned correctly to global variables with the expected names.

In the second test case `test_dataframes`, we assume the expected dataframe for sheet 'CPI' and compare it with the dataframe assigned to the corresponding global variable.

Both test cases will run the 'myFunc' function and then assert the expected results.