import unittest
from bqplot import pyplot as plt2


class MyFuncTestCase(unittest.TestCase):
    def test_y_axis_formatting(self):
        # Set up initial plot
        x_values = []
        y_values = []
        plt2.show()

        def functionThatIsCalledRepeatedly(x_val, y_val):
            x_values.append(x_val)
            y_values.append(y_val)
            plt2.plot(x_values, y_values)

        # Call function with sample data
        functionThatIsCalledRepeatedly(1, 1000000000)

        # Check if y-axis formatting is correct
        y_axis_format = plt2.axes()[1].tick_format
        expected_format = "0,0"
        self.assertEqual(y_axis_format, expected_format)

if __name__ == '__main__':
    unittest.main()