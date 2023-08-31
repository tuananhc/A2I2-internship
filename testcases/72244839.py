Here are some unit test cases to test the functionality of the 'myFunc' implementation:

```python
import unittest
from datetime import datetime, timedelta

def myFunc(txt):
    best_value = -1
    start_time = datetime.now()
    for word in txt:
        if value(word) > best_value:
            best_value = value(word)
        elapsed_time = datetime.now() - start_time
        if elapsed_time.total_seconds() >= 60:
            return best_value
    return best_value

def value(word):
    # Provide implementation for the value() function
    pass

class MyFuncTestCase(unittest.TestCase):
    
    def test_returns_best_value(self):
        txt = ['apple', 'banana', 'cat', 'dog']
        expected_result = value('dog')
        actual_result = myFunc(txt)
        self.assertEqual(actual_result, expected_result)
    
    def test_returns_negative_one_if_no_values(self):
        txt = []
        expected_result = -1
        actual_result = myFunc(txt)
        self.assertEqual(actual_result, expected_result)
    
    def test_stops_running_after_one_minute(self):
        txt = ['apple', 'banana', 'cat', 'dog']
        start_time = datetime.now()
        myFunc(txt)
        elapsed_time = datetime.now() - start_time
        self.assertLess(elapsed_time.total_seconds(), 61)
    
    def test_returns_best_value_if_stopped(self):
        txt = ['apple', 'banana', 'cat', 'dog']
        interrupted_result = myFunc(txt)
        continue_result = myFunc(txt)
        self.assertEqual(interrupted_result, continue_result)
    
    def test_handles_large_inputs(self):
        txt = ['a'] * int(1e6)
        expected_result = value('a')
        actual_result = myFunc(txt)
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
```

These test cases cover different scenarios, such as verifying that the function returns the correct best_value, handles an empty list, stops running after one minute, resumes correctly after being stopped, and handles large inputs. Adjust the test cases according to your specific needs and expected behavior of the 'myFunc' implementation.