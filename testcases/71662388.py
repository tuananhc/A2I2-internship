Here is a sample unit test case for the 'myFunc' function:

```python
import pandas as pd
import unittest

def myFunc(df):
    df['month'] = pd.to_datetime(df['date']).dt.strftime('%b')
    aggregated_df = df.groupby(['name', 'category']).pivot('month').agg({'count': 'sum', 'price': 'sum', 'revenue': 'sum'}).reset_index()
    return aggregated_df

class TestMyFunc(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame([["12", "10-01-2022", 'boot', "shoe", 100, 50],
                                ["211", "10-01-2022", 'sandal', "shoe", 210, 20],
                                ["321", "10-02-2022", 'boot', "shoe", 100, 45],
                                ["413", "10-02-2022", 'boot', "shoe", 100, 45],
                                ["15", "10-02-2022", 'dress', "cloth", 155, 95],
                                ["633", "10-03-2022", 'boot', "shoe", 75, 30],
                                ["247", "10-03-2022", 'boot', "shoe", 75, 30],
                                ["8787", "10-04-2022", 'boot', "shoe", 120, 45],
                                ["9232", "10-05-2022", 'shirt', "cloth", 75, 30],
                                ["12340", "10-05-2022", 'dress', "cloth", 175, 95]],
                               columns=["count", "date", "name", "category", "price", "revenue"])

    def test_myFunc(self):
        expected_output = pd.DataFrame([["boot", "shoe", 12, 734, 875, 100, 100, 75, 120, 0, 0, 0],
                                        ["dress", "cloth", 0, 15, 0, 0, 0, 0, 0, 155, 95],
                                        ["sandal", "shoe", 211, 0, 0, 210, 0, 0, 0, 0, 0],
                                        ["shirt", "cloth", 0, 0, 0, 0, 0, 0, 0, 75, 30]],
                                       columns=["name", "category", "Apr", "Feb", "Jan", "Mar", "May", "Apr", "Feb", "Jan", "Mar", "May"])
        
        self.assertTrue(expected_output.equals(myFunc(self.df)))

if __name__ == '__main__':
    unittest.main()
```

In this test case, we first define the 'myFunc' function that takes a dataframe as input and returns the aggregated dataframe.
Then, we create a class named 'TestMyFunc' for unit testing. Inside this class, we define a method named 'test_myFunc' which calls the 'myFunc' function with a sample dataframe and compares the output with the expected result using the 'assertTrue' assertion method from the unittest library.
Finally, in the '__main__' block, we run the test case using the 'unittest.main()' function.