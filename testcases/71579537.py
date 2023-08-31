Here are some unit test cases for the 'myFunc' function:

```python
import unittest

class MyFuncTestCase(unittest.TestCase):
    def test_case1(self):
        # Test with criteria: Column A > 2 and Column B >= 4
        # Expected output:
        #  Column A   Column B   Column C
        # --------------------------------
        #      1          4          1
        #      3          1          0
        #      4          5          2
        #      1          1          0
        expected_output = [
            [1, 4, 1],
            [3, 1, 0],
            [4, 5, 2],
            [1, 1, 0]
        ]
        
        input_data = [
            [1, 4],
            [3, 1],
            [4, 5],
            [1, 1]
        ]
        
        result = myFunc(input_data)
        
        self.assertEqual(result, expected_output)
    
    def test_case2(self):
        # Test with criteria: Column A > 10 and Column B >= 4
        # Expected output: Empty dataframe
        expected_output = []
        
        input_data = [
            [1, 4],
            [3, 1],
            [4, 5],
            [1, 1]
        ]
        
        result = myFunc(input_data)
        
        self.assertEqual(result, expected_output)
        
    def test_case3(self):
        # Test with an empty dataframe
        # Expected output: Empty dataframe
        expected_output = []
        
        input_data = []
        
        result = myFunc(input_data)
        
        self.assertEqual(result, expected_output)

unittest.main(argv=[''], exit=False)
```

Make sure to update the `myFunc` function to use the proper input and return types, and implement the logic as described in the task description.