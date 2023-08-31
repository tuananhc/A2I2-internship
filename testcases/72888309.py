Here are some unit test cases similar to the `unittest` library for the given task:

```python
import unittest
from unittest.mock import patch
from mymodule import myFunc

class MyFuncTestCase(unittest.TestCase):
    
    @patch('pyautogui.locateOnScreen')
    def test_if_image_found(self, mock_locateOnScreen):
        mock_locateOnScreen.return_value = (100, 100, 200, 200)  # Mocking the image location
        with patch('pyautogui.moveRel') as mock_moveRel:
            with patch('pyautogui.click') as mock_click:
                result = myFunc()
                mock_locateOnScreen.assert_called_with('ScheduledBy.png', confidence=0.9)
                mock_moveRel.assert_called_with(277, 25)
                mock_click.assert_called_once()
        self.assertEqual(result, "Image found and clicked")

    @patch('pyautogui.locateOnScreen')
    def test_if_image_not_found(self, mock_locateOnScreen):
        mock_locateOnScreen.return_value = None  # Mocking that image is not found
        with patch('builtins.print') as mock_print:
            result = myFunc()
            mock_locateOnScreen.assert_called_with('ScheduledBy.png', confidence=0.9)
            mock_print.assert_called_with("No")
        self.assertEqual(result, "Image not found")

if __name__ == "__main__":
    unittest.main()
```

Note: The above test cases assume that the `myFunc` function exists and is imported from a module named `mymodule`. Make sure to replace `mymodule` with the appropriate module name in your code.