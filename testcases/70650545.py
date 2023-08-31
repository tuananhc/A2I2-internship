# Here are the unit test cases for the 'myFunc' function:

# ```python
import pandas as pd
import unittest

def myFunc(df_chunk):
    x = df_chunk.groupby('id', dropna=True).agg(lambda x: list(x))
    return x

class MyFuncTestCase(unittest.TestCase):
    
    def test_with_null_values(self):
        df = pd.DataFrame({
            'id': [1, 1, 1],
            'surname': ['Bruce', None, None],
            'given_name': ['Erin', None, None],
            'date_of_birth': ['11/03/1961', '11/04/1961', '11/06/1961'],
            'address': ['10 Kestrel Wood Way, York', '4 Ward Avenue, Cowes', '11 Woodhill Court, Woodside Road, Amersham'],
            'postcode': ['YO31 9EJ', 'BD10 0LT', 'WA14 1LH'],
            'mobile': ['+64 21 421 2300', '+64 29 975 1551', '+64 22 5491 7112']
        })
        expected_df = pd.DataFrame({
            'surname': ['Bruce'],
            'given_name': ['Erin'],
            'date_of_birth': [['11/03/1961', '11/04/1961', '11/06/1961']],
            'address': [['10 Kestrel Wood Way, York', '4 Ward Avenue, Cowes', '11 Woodhill Court, Woodside Road, Amersham']],
            'postcode': [['YO31 9EJ', 'BD10 0LT', 'WA14 1LH']],
            'mobile': [['+64 21 421 2300', '+64 29 975 1551', '+64 22 5491 7112']]
        })
        
        result = myFunc(df)
        
        pd.testing.assert_frame_equal(result, expected_df)
    
    def test_without_null_values(self):
        df = pd.DataFrame({
            'id': [1, 1, 1],
            'surname': ['Bruce', 'Wayne', 'Banner'],
            'given_name': ['Erin', 'Bruce', 'Bruce'],
            'date_of_birth': ['11/03/1961', '11/04/1961', '11/06/1961'],
            'address': ['10 Kestrel Wood Way, York', '4 Ward Avenue, Cowes', '11 Woodhill Court, Woodside Road, Amersham'],
            'postcode': ['YO31 9EJ', 'BD10 0LT', 'WA14 1LH'],
            'mobile': ['+64 21 421 2300', '+64 29 975 1551', '+64 22 5491 7112']
        })
        expected_df = pd.DataFrame({
            'surname': ['Bruce'],
            'given_name': ['Erin'],
            'date_of_birth': [['11/03/1961', '11/04/1961', '11/06/1961']],
            'address': [['10 Kestrel Wood Way, York', '4 Ward Avenue, Cowes', '11 Woodhill Court, Woodside Road, Amersham']],
            'postcode': [['YO31 9EJ', 'BD10 0LT', 'WA14 1LH']],
            'mobile': [['+64 21 421 2300', '+64 29 975 1551', '+64 22 5491 7112']]
        })
        
        result = myFunc(df)
        
        pd.testing.assert_frame_equal(result, expected_df)

if __name__ == "__main__":
    unittest.main()
# ```

# You can run the tests by executing the script. If all tests pass, it means the 'myFunc' function is implemented correctly.