Here are some unit test cases that you can use to test your `mult_tuple` function:

```
import unittest

class TestMultTuple(unittest.TestCase):

    def test_mult_tuple(self):
        self.assertEqual(mult_tuple((1, 2), (4, 5)), ((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2)))
        
    def test_mult_tuple_same_tuples(self):
        self.assertEqual(mult_tuple((1, 2), (1, 2)), ((1, 1), (1, 2), (2, 1), (2, 2)))
        
    def test_mult_tuple_different_length_tuples(self):
        self.assertEqual(mult_tuple((1, 2, 3), (4, 5)), ((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2), (3, 4), (4, 3), (3, 5), (5, 3)))
        
    def test_mult_tuple_empty_tuples(self):
        self.assertEqual(mult_tuple((), (4, 5)), ())
        
    def test_mult_tuple_empty_input(self):
        self.assertEqual(mult_tuple((), ()), ())
        
if __name__ == '__main__':
    unittest.main()
```

Make sure to include the `unittest` module and run `unittest.main()` to execute the tests.