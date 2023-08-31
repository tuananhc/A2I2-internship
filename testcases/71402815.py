Here are some unit test cases for the 'myFunc' function:

```python
import unittest
import pandas as pd

def myFunc(w):
    data = []
    for item in w:
        second_string = item[1]
        first_char = second_string[0]
        num = second_string.split('=')[1].rstrip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        last_char = second_string.split('=')[1][-1]
        data.append([first_char, num, last_char])
    df = pd.DataFrame(data, columns=['First', 'Number', 'Last'])
    return df


class TestMyFunc(unittest.TestCase):

    def test_case1(self):
        w = [[['I=427', 'PLAN=1'], 'A=0PDB'],
             [['I=427', 'PLAN=1'], 'B=40NGC'],
             [['I=427', 'PLAN=1'], 'C=21#NGA'],
             [['I=429', 'PLAN=1'], 'A=0PDB'],
             [['I=429', 'PLAN=1'], 'B=18C'],
             [['I=429', 'PLAN=1'], 'C=28TGD'],
             [['I=429', 'PLAN=1'], 'D=18TGA'],
             [['I=429', 'PLAN=1'], 'E=1A'],
             [['I=429', 'PLAN=2'], 'A=0PDB'],
             [['I=429', 'PLAN=2'], 'B=17C']]
        expected_df = pd.DataFrame(
            [['A', '0', 'B'],
             ['B', '40', 'C'],
             ['C', '21', 'N'],
             ['A', '0', 'B'],
             ['B', '18', 'C'],
             ['C', '28', 'D'],
             ['D', '18', 'T'],
             ['E', '1', 'A'],
             ['A', '0', 'B'],
             ['B', '17', 'C']],
            columns=['First', 'Number', 'Last']
        )
        self.assertEqual(myFunc(w).equals(expected_df), True)

    def test_case2(self):
        w = [[['I=427', 'PLAN=1'], 'A=0XYZ'],
             [['I=427', 'PLAN=1'], 'B=1234PQR'],
             [['I=427', 'PLAN=1'], 'C=5'],
             [['I=429', 'PLAN=1'], 'A=0'],
             [['I=429', 'PLAN=1'], 'B=999ABC'],
             [['I=429', 'PLAN=1'], 'C=3XZ'],
             [['I=429', 'PLAN=1'], 'D=9'],
             [['I=429', 'PLAN=1'], 'E=2Y'],
             [['I=429', 'PLAN=2'], 'A=1PQR'],
             [['I=429', 'PLAN=2'], 'B=0RST']]
        expected_df = pd.DataFrame(
            [['A', '0', 'X'],
             ['B', '1234', 'P'],
             ['C', '5', ''],
             ['A', '0', ''],
             ['B', '999', 'A'],
             ['C', '3', 'X'],
             ['D', '9', ''],
             ['E', '2', 'Y'],
             ['A', '1', 'P'],
             ['B', '0', 'R']],
            columns=['First', 'Number', 'Last']
        )
        self.assertEqual(myFunc(w).equals(expected_df), True)


if __name__ == '__main__':
    unittest.main()
```

These unit test cases test the 'myFunc' function with different inputs and compare the output with the expected pandas DataFrame. The test cases cover different scenarios including cases with special characters, empty strings, and different lengths of strings after the equal sign.