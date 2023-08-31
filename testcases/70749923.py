Here are some unit test cases that you can use to test the 'wait_until_complete' function with different arguments using the unittest library:

```python
import unittest
from unittest.mock import MagicMock

def wait_until_complete(uid, time):
    # function implementation
    pass

class MyTestCase(unittest.TestCase):

    def test_wait_until_complete_called(self):
        # Create a mock object for the function
        mock_wait_until_complete = MagicMock()

        # Call the function that is being tested
        myFunc()

        # Assert that the function wait_until_complete was called
        mock_wait_until_complete.assert_called()

    def test_wait_until_complete_called_with_arguments(self):
        # Create a mock object for the function
        mock_wait_until_complete = MagicMock()

        # Call the function that is being tested
        myFunc()

        # Assert that the function wait_until_complete was called with specified arguments
        mock_wait_until_complete.assert_called_with('uid', 123)

    def test_wait_until_complete_called_with_any_arguments(self):
        # Create a mock object for the function
        mock_wait_until_complete = MagicMock()

        # Call the function that is being tested
        myFunc()

        # Assert that the function wait_until_complete was called with any arguments
        mock_wait_until_complete.assert_called_with(any(str), any(int)))


if __name__ == '__main__':
    unittest.main()
```

Note: The 'mock_wait_until_complete' object is used to mock the actual function 'wait_until_complete', so we can assert if it was called or called with specific arguments.