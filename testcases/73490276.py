Here are the unit test cases for the 'myFunc' function to drop rows with time='09:15' from the given DataFrame:

```python
import unittest
import pandas as pd

def myFunc(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = df['Date'].dt.time
    df_filtered = df[df['Time'] != datetime.time(9, 15)]

    return df_filtered


class TestMyFunc(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Date': ['2022-08-08 09:15:00', '2022-08-10 13:15:00', '2022-08-12 09:15:00', '2022-08-18 09:15:00'],
            'Open': [17397.39, 17508.28, 17651.81, 17934.37],
            'High': [17443.70, 17532.00, 17680.70, 17954.65],
            'Low': [17359.75, 17479.55, 17597.85, 17863.45],
            'Close': [17411.06, 17510.24, 17654.14, 17914.30],
            'Volume': [0, 0, 0, 0]
        })

    def test_drop_rows_with_9_15_time(self):
        expected_df = pd.DataFrame({
            'Date': ['2022-08-10 13:15:00', '2022-08-18 09:15:00'],
            'Open': [17508.28, 17934.37],
            'High': [17532.00, 17954.65],
            'Low': [17479.55, 17863.45],
            'Close': [17510.24, 17914.30],
            'Volume': [0, 0]
        })

        actual_df = myFunc(self.df)
        pd.testing.assert_frame_equal(actual_df, expected_df)


if __name__ == '__main__':
    unittest.main()
```

Make sure to have the `pandas` library installed in your Python environment to run the tests.