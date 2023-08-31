Sure! Here's an example of how you can write unit test cases for the `myFunc` function using the `unittest` library:

```python
import unittest

def myFunc():
    # Your code here

class MyFuncTestCase(unittest.TestCase):
    def test_table_creation(self):
        # Test case for table creation
        table = myFunc()
        
        # Assert the correct number of questions
        self.assertEqual(len(table), 3)
        
        # Assert the correct structure of the table
        self.assertIn('Q1', table)
        self.assertIn('Q2', table)
        self.assertIn('Q3', table)
        
        # Assert the correct number of columns
        self.assertEqual(len(table['Q1'].columns), 4)
        self.assertEqual(len(table['Q2'].columns), 4)
        self.assertEqual(len(table['Q3'].columns), 4)
        
        # Assert the correct number of rows for each question
        self.assertEqual(len(table['Q1'].index), 2)
        self.assertEqual(len(table['Q2'].index), 2)
        self.assertEqual(len(table['Q3'].index), 2)
        
        # Assert the correct values in the table
        self.assertEqual(table['Q1']['#Res']['M'], 2)
        self.assertEqual(table['Q1']['#Res']['F'], 2)
        self.assertEqual(table['Q1']['%Rep']['M'], 50)
        self.assertEqual(table['Q1']['%Rep']['F'], 50)
        # Repeat the above assertions for Q2 and Q3

if __name__ == '__main__':
    unittest.main()
```

This example demonstrates how you can test the table creation functionality of your `myFunc` function. You can add more test cases to cover other aspects of the function's behavior.