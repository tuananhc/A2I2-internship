Here are some sample unit test cases for the given task:

```python
import unittest
from unittest.mock import patch
import os
import pandas as pd

# Import the function to be tested
from myFunc import selectPath, create_subfolder, openFile

class MyFuncTestCase(unittest.TestCase):

    @patch('myFunc.askdirectory', return_value='/path/to/directory')
    def test_selectPath(self, mock_askdirectory):
        selectPath()
        self.assertEqual(path.get(), '/path/to/directory')
    
    def test_create_subfolder(self):
        path.set('/path/to/directory')
        folder.set('new_subfolder')
        create_subfolder()
        expected_path = os.path.join('/path/to/directory', 'new_subfolder')
        self.assertEqual(dirs, expected_path)
    
    @patch('myFunc.filedialog.askopenfilename', return_value='/path/to/file.xlsx')
    @patch('myFunc.os.startfile')
    @patch('myFunc.pd.read_excel')
    def test_openFile(self, mock_read_excel, mock_startfile, mock_askopenfilename):
        filename = '/path/to/file.xlsx'
        sheet_name = 'Order Details'
        filepath = os.path.join(path.get(), folder.get(), 'Intelliscan.xlsx')
      
        openFile()
        
        mock_askopenfilename.assert_called_once_with(initialdir=r'L:\folder\My_file', filetypes=[("Excel Files", "*.xlsx")])
        mock_startfile.assert_called_once_with(filename)
        mock_read_excel.assert_called_once_with(filename, sheet_name=sheet_name)
        df.to_excel.assert_called_once_with(filepath, index=False)

if __name__ == '__main__':
    unittest.main()
```
Note: 
- In each test case, we use the `patch` decorator from the `unittest.mock` module to mock the external dependencies used within the respective function being tested.
- You may need to modify the imports and importing behavior based on the structure of your code and the dependencies used.