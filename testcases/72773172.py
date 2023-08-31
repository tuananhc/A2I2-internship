Below are some unit test cases for the given task:

```python
import unittest
from myFunc import calculate_file

class TestCalculateFile(unittest.TestCase):

    def test_sheet_df_length(self):
        sheet_df = calculate_file()
        self.assertEqual(len(sheet_df), 200)  # 5 rows * 40 dataframes = 200

    def test_excel_file(self):
        calculate_file()
        excel_file = pd.read_excel('output_file.xlsx', sheet_name=None)
        self.assertEqual(len(excel_file), 40)  # 40 sheet names

        for i in range(1, 41):
            sheet_name = f'Sheet {i}'
            self.assertIn(sheet_name, excel_file)  # check if sheet name exists

            df = excel_file[sheet_name]
            self.assertEqual(len(df), 5)  # each sheet should have 5 rows
            self.assertEqual(df.shape[1], 3)  # each sheet should have 3 columns

if __name__ == '__main__':
    unittest.main()
```

Make sure to replace `'myFunc'` with the actual module or script name where `calculate_file` function is defined. Also, don't forget to install the `pandas` library and import it into the test file.