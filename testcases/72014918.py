import unittest
  
class MyFuncTestCase(unittest.TestCase):
    
    def test_myFunc_returns_correct_output(self):
        # Arrange
        input_data = {
            'ID': [0, 0, 0, 0, 0, 1, 1, 1, 2, 2],
            'date': ['2022-01-03 10:00:01', '2022-01-03 11:00:01', '2022-01-03 11:10:01', 
                     '2022-01-03 12:00:03', '2022-01-03 14:32:01', '2022-01-03 10:32:01', 
                     '2022-01-04 11:32:01', '2022-01-04 14:32:01', '2022-01-02 08:00:01', 
                     '2022-01-02 08:02:01'],
            'direction': ['IN', 'IN', 'OUT', 'IN', 'OUT', 'OUT', 'IN', 'OUT', 'OUT', 'IN']
        }
        expected_output = {
            'ID': [0, 0, 1],
            'entry_date': ['2022-01-03 10:00:01', '2022-01-03 12:00:03', '2022-01-04 11:32:01'],
            'exit_date': ['2022-01-03 11:10:01', '2022-01-03 14:32:01', '2022-01-04 14:32:01']
        }
        
        # Act
        result = myFunc(input_data)
        
        # Assert
        self.assertEqual(result, expected_output)
    
    def test_myFunc_returns_empty_output_for_no_input(self):
        # Arrange
        input_data = {
            'ID': [],
            'date': [],
            'direction': []
        }
        expected_output = {
            'ID': [],
            'entry_date': [],
            'exit_date': []
        }
        
        # Act
        result = myFunc(input_data)
        
        # Assert
        self.assertEqual(result, expected_output)
    
    def test_myFunc_handles_multiple_groups(self):
        # Arrange
        input_data = {
            'ID': [0, 0, 0, 1, 1, 1, 2, 2, 2],
            'date': ['2022-01-01 10:00:01', '2022-01-01 11:00:01', '2022-01-01 11:10:01', 
                     '2022-01-02 10:00:01', '2022-01-02 11:00:01', '2022-01-02 11:10:01',
                     '2022-01-03 10:00:01', '2022-01-03 11:00:01', '2022-01-03 11:10:01'],
            'direction': ['IN', 'IN', 'OUT', 'IN', 'IN', 'OUT', 'IN', 'IN', 'OUT']
        }
        expected_output = {
            'ID': [0, 1, 2],
            'entry_date': ['2022-01-01 10:00:01', '2022-01-02 10:00:01', '2022-01-03 10:00:01'],
            'exit_date': ['2022-01-01 11:10:01', '2022-01-02 11:10:01', '2022-01-03 11:10:01']
        }
        
        # Act
        result = myFunc(input_data)
        
        # Assert
        self.assertEqual(result, expected_output)
  
if __name__ == '__main__':
    unittest.main()