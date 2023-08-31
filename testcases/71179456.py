Here are some basic unit test cases for the given task:

```python
import unittest
from unittest.mock import patch
from myScript import myFunc

class TestMyScript(unittest.TestCase):
    
    @patch('builtins.print')
    @patch('myScript.myFunc')
    def test_myFunc_called_once(self, mock_myFunc, mock_print):
        myFunc()
        mock_myFunc.assert_called_once()
    
    @patch('builtins.print')
    @patch('myScript.myFunc')
    def test_myFunc_return_value(self, mock_myFunc, mock_print):
        mock_myFunc.return_value = "Hello World"
        self.assertEqual(myFunc(), "Hello World")
    
if __name__ == '__main__':
    unittest.main()
```

Note: 
1. Replace `myScript` with the actual name of the Python script containing the `myFunc` function.
2. The test cases use the `patch` decorator from the `unittest.mock` module to mock the external dependencies (`print` function and `myFunc` function) and only test the logic of `myFunc` in isolation.