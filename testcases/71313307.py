Here are some unit test cases for the task of replacing column values in a Spark DataFrame:

```python
import unittest
from pyspark.sql import SparkSession
from my_module import myFunc

class DataFrameTests(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.getOrCreate()
        data = [["1", "xxx", "company 0"],
                ["2", "xxx", "company 1"],
                ["3", "company 44", "company 2"],
                ["4", "xxx", "company 1"],
                ["5", "bobby", "company 1"]]
        self.dataframe = self.spark.createDataFrame(data)

    def test_replace_column_values_single_column(self):
        # Replace "company" with "cmp" in a single column
        actual_df = myFunc(self.dataframe, "company", "cmp", "col1")
        
        expected_data = [["1", "xxx", "cmp 0"],
                         ["2", "xxx", "cmp 1"],
                         ["3", "company 44", "cmp 2"],
                         ["4", "xxx", "cmp 1"],
                         ["5", "bobby", "cmp 1"]]
        expected_df = self.spark.createDataFrame(expected_data)
        
        self.assertTrue(expected_df.collect() == actual_df.collect())

    def test_replace_column_values_all_columns(self):
        # Replace "company" with "cmp" in all columns
        actual_df = myFunc(self.dataframe, "company", "cmp", None)
        
        expected_data = [["1", "xxx", "cmp 0"],
                         ["2", "xxx", "cmp 1"],
                         ["3", "cmp 44", "cmp 2"],
                         ["4", "xxx", "cmp 1"],
                         ["5", "bobby", "cmp 1"]]
        expected_df = self.spark.createDataFrame(expected_data)
        
        self.assertTrue(expected_df.collect() == actual_df.collect())
    
    def tearDown(self):
        self.spark.stop()

if __name__ == '__main__':
    unittest.main()
```

Make sure to replace `my_module` with the actual name of the module in which your `myFunc` function is defined.