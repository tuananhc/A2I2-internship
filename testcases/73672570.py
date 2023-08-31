Here are some possible unit test cases for the 'myFunc' function:

```python
import unittest

class MyFuncTestCase(unittest.TestCase):
    def test_empty_df(self):
        df_a = pd.DataFrame(columns=['id', 'A', 'B', 'C'])
        df_b = pd.DataFrame(columns=['id', 'A', 'B', 'C'])
        df_c = pd.DataFrame(columns=['id', 'A', 'B', 'C'])
        search_list = ["A", "B", "C"]
        expected_output = [{'A': 0}, {'B': 0}, {'C': 0}]
        self.assertEqual(myFunc(df_a, df_b, df_c, search_list), expected_output)

    def test_non_empty_dfs(self):
        df_a = pd.DataFrame({'id': [1, 2], 'A': [2, 3], 'B': [2, 3], 'C': [2, 3]})
        df_b = pd.DataFrame({'id': [1, 2, 3, 4], 'A': [5, 6, 8, 0], 'B': [5, 6, 8, 0], 'C': [5, 6, 8, 0]})
        df_c = pd.DataFrame({'id': [1], 'A': [6], 'B': [6], 'C': [6]})
        search_list = ["A", "B", "C"]
        expected_output = [{'A': 2}, {'B': 4}, {'C': 1}]
        self.assertEqual(myFunc(df_a, df_b, df_c, search_list), expected_output)

    def test_search_list_with_invalid_columns(self):
        df_a = pd.DataFrame({'id': [1, 2], 'A': [2, 3], 'B': [2, 3], 'C': [2, 3]})
        df_b = pd.DataFrame({'id': [1, 2, 3, 4], 'A': [5, 6, 8, 0], 'B': [5, 6, 8, 0], 'C': [5, 6, 8, 0]})
        df_c = pd.DataFrame({'id': [1], 'A': [6], 'B': [6], 'C': [6]})
        search_list = ["D", "E", "F"]
        expected_output = [{'D': 0}, {'E': 0}, {'F': 0}]
        self.assertEqual(myFunc(df_a, df_b, df_c, search_list), expected_output)

if __name__ == '__main__':
    unittest.main()
```
These test cases cover scenarios such as empty dataframes, non-empty dataframes, and invalid columns in the search list.