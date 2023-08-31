To check if a function is being called irrespective of the arguments passed, you can use `mock.call()` instead of `assert_called()`. Here's an example:

```python
# Assuming you have a mock object called mock_wait_until_complete
# Mock the function call
mock_wait_until_complete.assert_called()

# Check if the function was called with any arguments
mock_wait_until_complete.assert_called_with()

# Alternatively, check if the function was called with any arguments using mock.call()
mock_wait_until_complete.assert_called_once_with(mock.call())
```

By using `mock.call()`, you can assert that the function was called with any arguments, regardless of the actual values. This way, the test case will pass regardless of the arguments passed to the function.

Edit:
To ignore the specific argument values in the assertion, you can use `ANY` from the `mock` module. Here's an example:

```python
from unittest.mock import ANY

# Assuming you have a mock object called mock_wait_until_complete
# Check if the function was called with any arguments
mock_wait_until_complete.assert_called_with(ANY, ANY)
```

In this example, the `ANY` argument in `assert_called_with()` will match any argument value. Therefore, the test case will pass irrespective of the specific argument values.