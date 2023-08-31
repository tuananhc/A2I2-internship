Here are some unit test cases for the 'myFunc' function:

1. Test case: Testing if non-missing values are correctly detected
```python
import pandas as pd
import numpy as np
import unittest

class MyFuncTest(unittest.TestCase):
    def test_detect_non_missing_values(self):
        df = pd.DataFrame(dict(age=[5, 6, np.NaN], born=[pd.NaT, pd.Timestamp('1939-05-27'), pd.Timestamp('1940-04-25')], name=['Alfred', 'Batman', ''], toy=[None, 'Batmobile', 'Joker']))
        result = myFunc(df)
        expected = pd.DataFrame({'age': [True, True, False], 'born': [False, True, True], 'name': [True, True, False], 'toy': [False, True, True]})
        self.assertEqual(result, expected)

unittest.main(argv=[''], exit=False)
```

2. Test case: Testing if the string prefix is correctly added to non-missing values
```python
import pandas as pd
import numpy as np
import unittest

class MyFuncTest(unittest.TestCase):
    def test_add_string_prefix(self):
        df = pd.DataFrame(dict(age=[5, 6, np.NaN], born=[pd.NaT, pd.Timestamp('1939-05-27'), pd.Timestamp('1940-04-25')], name=['Alfred', 'Batman', ''], toy=[None, 'Batmobile', 'Joker']))
        result = myFunc(df)
        expected = pd.DataFrame({'age': ['+5.0', np.NaN, '+Alfred'], 'born': [pd.NaT, '+1939-05-27', '+Batman'], 'name': ['+', '+', '+'], 'toy': [np.NaN, '+Batmobile', '+Joker']})
        self.assertEqual(result, expected)

unittest.main(argv=[''], exit=False)
```

3. Test case: Testing if the returned dataframe has the same dimensions as the input dataframe
```python
import pandas as pd
import numpy as np
import unittest

class MyFuncTest(unittest.TestCase):
    def test_dataframe_dimensions(self):
        df = pd.DataFrame(dict(age=[5, 6, np.NaN], born=[pd.NaT, pd.Timestamp('1939-05-27'), pd.Timestamp('1940-04-25')], name=['Alfred', 'Batman', ''], toy=[None, 'Batmobile', 'Joker']))
        result = myFunc(df)
        self.assertEqual(result.shape, df.shape)

unittest.main(argv=[''], exit=False)
```

These test cases cover the detection of non-missing values, adding a string prefix to non-missing values, and checking if the dimensions of the returned dataframe match the input dataframe.