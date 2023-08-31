Here are some test cases you can generate using the unittest library for the 'myFunc' function:

```python
import unittest
import pandas as pd

def myFunc(datajson):
    # your implementation here
    pass

class MyFuncTestCase(unittest.TestCase):
    def test_correct_dataframe_columns(self):
        datajson= {
            "10001": {
                "extra": {"user": "Tom"},
                "data":{"A":5, "B":10}
            },
            "10002":{
                "extra": {"user": "Ben"},
                "data":{"A":7, "B":20}
            },
            "10003":{
                "extra": {"user": "Ben"},
                "data":{"A":6, "B":15}
            }
        }

        expected_columns = ['10001_extra_user', '10001_data_A', '10001_data_B',
                            '10002_extra_user', '10002_data_A', '10002_data_B',
                            '10003_extra_user', '10003_data_A', '10003_data_B']

        df = myFunc(datajson)
        self.assertListEqual(list(df.columns), expected_columns)

    def test_correct_dataframe_values(self):
        datajson= {
            "10001": {
                "extra": {"user": "Tom"},
                "data":{"A":5, "B":10}
            },
            "10002":{
                "extra": {"user": "Ben"},
                "data":{"A":7, "B":20}
            },
            "10003":{
                "extra": {"user": "Ben"},
                "data":{"A":6, "B":15}
            }
        }

        expected_values = [['Tom', 5, 10],
                          ['Ben', 7, 20],
                          ['Ben', 6, 15]]

        df = myFunc(datajson)
        self.assertListEqual(df.values.tolist(), expected_values)

    def test_empty_datajson(self):
        datajson = {}

        df = myFunc(datajson)
        self.assertEqual(len(df.columns), 0)

    def test_invalid_datajson(self):
        datajson = {
            "10001": {
                "extra": {"user": "Tom"},
                "data":{"A":5, "B":10}
            },
            "10002":{
                "extra": {"user": "Ben"},
                "data":{"A":7}
            },
            "10003":{
                "extra": {"user": "Ben"},
                "data":{"B":15}
            }
        }

        df = myFunc(datajson)
        self.assertEqual(len(df.columns), 6)

if __name__ == '__main__':
    unittest.main()
```

These test cases cover scenarios such as:
- Checking if the DataFrame has the correct columns after flattening the JSON data.
- Checking if the DataFrame values match the expected values.
- Testing for an empty `datajson`.
- Testing for invalid `datajson` with missing or incomplete data.