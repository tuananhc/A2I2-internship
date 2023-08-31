Here are some test cases for the 'myFunc' function that you can use to test the behavior of the program:

```python
import unittest
from PIL import Image
from inky import InkyWHAT

class MyFuncTestCase(unittest.TestCase):

    def test_display_image(self):
        inky_display = InkyWHAT("yellow")
        image_path = "/home/pi/Desktop/test2.jpg"

        # Call myFunc here passing inky_display and image_path parameters
        result = myFunc(inky_display, image_path)

        # Assert the expected output of the function
        # You can validate the expected behavior using assert statements
        self.assertEqual(result, "<expected_result>")

    def test_image_size(self):
        inky_display = InkyWHAT("yellow")
        image_path = "/home/pi/Desktop/test2.jpg"
        expected_size = (400, 300)  # Set the expected size based on the provided code

        # Call myFunc here passing inky_display and image_path parameters
        result = myFunc(inky_display, image_path)

        # Assert the expected output of the function
        self.assertEqual(result.size, expected_size)

    def test_image_mode(self):
        inky_display = InkyWHAT("yellow")
        image_path = "/home/pi/Desktop/test2.jpg"
        expected_mode = "RGB"  # Set the expected mode based on the provided code

        # Call myFunc here passing inky_display and image_path parameters
        result = myFunc(inky_display, image_path)

        # Assert the expected output of the function
        self.assertEqual(result.mode, expected_mode)

if __name__ == '__main__':
    unittest.main()
```

Note: Replace `"<expected_result>"` with the actual expected output of the function for the `test_display_image` test case. Also, make sure to import the `myFunc` function in your test file and modify the test cases accordingly if `myFunc` is not within the same scope.