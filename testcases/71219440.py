Here are some unit test cases for the given task using the `unittest` library in Python:

```python
import unittest

def myFunc():
    # Your program logic here
    sum_of_numbers = sum(range(1, 8))
    return sum_of_numbers

class MyFuncTestCase(unittest.TestCase):
    def test_sum_of_7_numbers(self):
        self.assertEqual(myFunc(), 28)

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `myFunc` function represents the program logic that calculates the sum of 7 natural numbers (1+2+3+4+5+6+7). The `test_sum_of_7_numbers` method is a testcase within the `MyFuncTestCase` class, which checks if the returned result from `myFunc` is equal to 28 (the expected output). The `unittest` library is used to execute these testcases.