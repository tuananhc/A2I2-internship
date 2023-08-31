Here are some unit test cases for the given task:

```python
import unittest

def myFunc():
    a = None
    b = 0
    while a != 0:
        a = int(input("Enter a number: "))
        b = b + a
    print("The total sum of the numbers are {}".format(b))

class MyFuncTest(unittest.TestCase):
    def test_sum_of_numbers(self):
        # Set up input values
        inputs = ['1', '2', '3', '0']
        expected_output = 'The total sum of the numbers are 6'

        # Redirect input values
        original_input = __builtins__.input
        __builtins__.input = lambda _: inputs.pop(0)

        # Redirect standard output
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        # Call the function
        myFunc()

        # Restore standard output
        sys.stdout = original_stdout

        # Assert the output
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_non_integer_input(self):
        # Set up input values
        inputs = ['1', 'a', '2', '0']
        expected_output = 'The total sum of the numbers are 3'

        # Redirect input values
        original_input = __builtins__.input
        __builtins__.input = lambda _: inputs.pop(0)

        # Redirect standard output
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        # Call the function
        myFunc()

        # Restore standard output
        sys.stdout = original_stdout

        # Assert the output
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
```

These test cases cover two scenarios:
1. `test_sum_of_numbers` - It checks if the function correctly calculates the sum of the numbers when only integers ('1', '2', '3') are given as input.
2. `test_non_integer_input` - It checks if the function correctly handles the scenario when a non-integer ('a') is given as input, and the code prints the expected output (sum of valid integers).

Note: In the test cases, the `myFunc()` function is called directly, but in an actual implementation, you might call it from another function or use suitable arguments/return values according to your needs.