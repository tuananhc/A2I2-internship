Here are some unit test cases for the `myFunc` function:

```python
import unittest

class MyFuncTestCase(unittest.TestCase):
    
    def test_index_above_threshold(self):
        demo_list = [1, 1, 3, 5, 8, 13]
        threshold = 4
        expected_index = 3
        
        result = myFunc(demo_list, threshold)
        
        self.assertEqual(result, expected_index)
    
    def test_index_below_threshold(self):
        demo_list = [1, 1, 3, 5, 8, 13]
        threshold = 2
        expected_index = None
        
        result = myFunc(demo_list, threshold)
        
        self.assertEqual(result, expected_index)
    
    def test_empty_list(self):
        demo_list = []
        threshold = 5
        expected_index = None
        
        result = myFunc(demo_list, threshold)
        
        self.assertEqual(result, expected_index)
    
    def test_all_values_above_threshold(self):
        demo_list = [7, 9, 11, 13, 15]
        threshold = 5
        expected_index = 0
        
        result = myFunc(demo_list, threshold)
        
        self.assertEqual(result, expected_index)

if __name__ == '__main__':
    unittest.main()
```

The above code assumes that you will be using the unittest library for testing. It contains 4 test cases:

1. `test_index_above_threshold`: Tests if the function returns the correct index when there is a value above the threshold.
2. `test_index_below_threshold`: Tests if the function returns `None` when there is no value above the threshold.
3. `test_empty_list`: Tests if the function returns `None` when the list is empty.
4. `test_all_values_above_threshold`: Tests if the function returns the correct index when all values in the list are above the threshold.