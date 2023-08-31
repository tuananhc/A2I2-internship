Here are some sample unit test cases for the task:

```python
import unittest
import random

class MyFuncTestCase(unittest.TestCase):

    def test_replace_random_a_with_b(self):
        alphabets = ["a", "c", "a", "a", "b", "c"]
        result = myFunc(alphabets)
        self.assertEqual(len(result), len(alphabets))  # Test if the length of the result is the same as the original list
        self.assertIn("b", result)  # Test if the result contains at least one "b" element

    def test_replace_random_a_with_b_multiple_times(self):
        alphabets = ["a", "c", "a", "a", "b", "c"]
        original_count_a = alphabets.count("a")
        result = myFunc(alphabets)
        new_count_a = result.count("a")
        self.assertEqual(original_count_a, new_count_a)  # Test if the count of "a" remains the same after replacement

    def test_replace_random_a_with_b_random_index(self):
        alphabets = ["a", "c", "a", "a", "b", "c"]
        random.seed(123)  # Set a seed for predictable random index generation
        random_index = random.randint(0, len(alphabets) - 1)
        result = myFunc(alphabets)
        self.assertEqual(result[random_index], "b")  # Test if the random index is replaced with "b"

if __name__ == '__main__':
    unittest.main()
```

Make sure to replace `myFunc` with the name of your actual function. You can run these test cases by executing the Python script or using a test runner like `unittest` from the command line.