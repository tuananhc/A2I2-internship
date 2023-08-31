Here are some unit test cases for the 'myFunc' function:

```python
import pandas as pd
import unittest

data_dict = {
    'ON': {'time': '2022-03-29 23:00:00', 'atm': 0.0895, 'rr25': -0.008, 'bf25': 0.0015, 'rr10': -0.014, 'bf10': 0.004},
    '1W': {'time': '2022-03-29 23:00:00', 'atm': 0.0785, 'rr25': -0.01, 'bf25': 0.002, 'rr10': -0.017, 'bf10': 0.0065},
    '2W': {'time': '2022-03-29 23:00:00', 'atm': 0.0795, 'rr25': -0.011, 'bf25': 0.0025, 'rr10': -0.019, 'bf10': 0.00837},
    '1M': {'time': '2022-03-29 23:00:00', 'atm': 0.077, 'rr25': -0.0115, 'bf25': 0.0025, 'rr10': -0.0207, 'bf10': 0.00925},
    '2M': {'time': '2022-03-29 23:00:00', 'atm': 0.075, 'rr25': -0.0115, 'bf25': 0.0025, 'rr10': -0.0207, 'bf10': 0.00937},
    '3M': {'time': '2022-03-29 23:00:00', 'atm': 0.07325, 'rr25': -0.012, 'bf25': 0.00255, 'rr10': -0.0222, 'bf10': 0.00969},
    '6M': {'time': '2022-03-29 23:00:00', 'atm': 0.07175, 'rr25': -0.0125, 'bf25': 0.00265, 'rr10': -0.02375, 'bf10': 0.0102},
    '9M': {'time': '2022-03-29 23:00:00', 'atm': 0.07125, 'rr25': -0.0125, 'bf25': 0.00295, 'rr10': -0.02375, 'bf10': 0.0115},
    '1Y': {'time': '2022-03-29 23:00:00', 'atm': 0.071, 'rr25': -0.0125, 'bf25': 0.003, 'rr10': -0.02381, 'bf10': 0.0117},
    '2Y': {'time': '2022-03-29 23:00:00', 'atm': 0.072, 'rr25': -0.0125, 'bf25': 0.0032, 'rr10': -0.02375, 'bf10': 0.01248}
}

expected_df = pd.DataFrame.from_dict(data_dict, orient='index')

class TestMyFunc(unittest.TestCase):

    def test_output_type(self):
        result = myFunc(data_dict)
        self.assertIsInstance(result, pd.DataFrame)

    def test_output_shape(self):
        result = myFunc(data_dict)
        self.assertEqual(result.shape, expected_df.shape)

    def test_output_columns(self):
        result = myFunc(data_dict)
        self.assertListEqual(result.columns.tolist(), expected_df.columns.tolist())

    def test_output_values(self):
        result = myFunc(data_dict)
        pd.testing.assert_frame_equal(result, expected_df)

if __name__ == "__main__":
    unittest.main()
```

In these test cases:
- The `test_output_type` case checks if the result of `myFunc` is an instance of a pandas DataFrame.
- The `test_output_shape` case checks if the shape of the result matches the expected shape of the DataFrame.
- The `test_output_columns` case checks if the columns of the result match the expected columns of the DataFrame.
- The `test_output_values` case compares the values of the result DataFrame with the expected DataFrame using `pd.testing.assert_frame_equal` for a comprehensive comparison.

You can modify these test cases as per your requirements and add more test cases if needed.