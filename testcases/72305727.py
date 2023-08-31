Here are some unit test cases similar to the unittest library for the task:

```python
import unittest
import numpy as np
import pandas as pd

class TestDataframe(unittest.TestCase):

    def setUp(self):
        self.x = np.random.randint(2, size=1000).reshape(500,2)
        self.data = pd.DataFrame(self.x ,columns=['x','y'])

    def test_pivot_table_return_type(self):
        result = myFunc(self.data)
        self.assertIsInstance(result, pd.DataFrame)

    def test_pivot_table_shape(self):
        result = myFunc(self.data)
        self.assertEqual(result.shape, (2, 2))

    def test_pivot_table_data(self):
        result = myFunc(self.data)
        expected_data = pd.DataFrame([[count, count], [count, count]],
                                     columns=[0, 1])
        pd.testing.assert_frame_equal(result, expected_data)

if __name__ == '__main__':
    unittest.main()
```

Make sure to replace `myFunc` with the actual function name that performs the desired pivot table operation. Additionally, you may need to modify the expected_data variable to match the expected output for your specific use case.