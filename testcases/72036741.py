Here are some sample unit test cases that you can use to test your function:

```python
import unittest

from myFunc import get_records

class TestGetRecords(unittest.TestCase):
    def test_total_budget(self):
        expected_result = 135 + 90 + 100 + 70 + 85
        actual_result = sum(row[2] for row in get_records())
        
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
```

In this example, we import the `unittest` library and define a test class `TestGetRecords` that inherits from `unittest.TestCase`. Inside this class, we define a test method `test_total_budget` which calculates the expected result by summing the third column of the records in `get_records()`. Then, we use the `assertEqual()` method to compare the actual result with the expected result.

To run the test cases, you can execute the test module by running `python -m unittest test_module.py` in the command line, replacing `test_module.py` with the name of your test module file.