```python
import unittest

def myFunc():
    ser_original = pd.Series([1.0, 2.0, np.nan, 4.0, 5.0], dtype=float)
    ser_imputed = ser_original.fillna(np.mean)
    return ser_imputed

class MyFuncTestCase(unittest.TestCase):
    def test_dtype_float(self):
        result = myFunc()
        self.assertEqual(result.dtype, np.float64)

if __name__ == '__main__':
    unittest.main()
```