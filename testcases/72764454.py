import unittest

def myFunc(data):
    # Your code here to change the values of alpha and alphanumeric cells to the mean of each column or any numeric value
    return modified_data

class MyFuncTestCase(unittest.TestCase):

    def setUp(self):
        self.data = [
            [1, 2, 5, 'f5'],
            [5, 'e5', 9, 6],
            ['tg', 56, 8, 'r5'],
            ['q2', 4, 75, 'g']
        ]

    def test_myFunc(self):
        expected_result = [
            [1, 2, 5, 3.5],
            [5, 27.5, 9, 6],
            [2.5, 56, 8, 3.5],
            [2.5, 4, 75, 3.5]
        ]
        self.assertEqual(myFunc(self.data), expected_result)

if __name__ == '__main__':
    unittest.main()