import unittest
import pandas as pd

# Define a sample dictionary and dataframes
dict_1 = {
    '2014-03-01': {
        'group_1': pd.DataFrame([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
                                [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 
                                [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], 
                                [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]]),
        'group_2': pd.DataFrame([[61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], 
                                [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]])},
    '2014-04-01': {
        'group_1': pd.DataFrame([[91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105], 
                                [106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120], 
                                [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135], 
                                [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]])},
    '2014-05-01': {
        'group_1': pd.DataFrame([[151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165], 
                                [166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180]])}
}

# Define the function to extract data to Excel
def extract_data_to_excel(file_name, data_dict, variables):
    writer = pd.ExcelWriter(file_name)
    
    for key in data_dict:
        # Create new sheet with the key as the sheet name
        data_dict[key].to_excel(writer, sheet_name=key)
        
        # Loop over groups to extract data to the sheet
        for group_key in data_dict[key]:
            group_data = data_dict[key][group_key]
            
            # Only extract the specified variables
            extracted_data = group_data[variables]
            
            # Get the current sheet by name
            sheet = writer.sheets[key]
            
            # Write the extracted data to the sheet
            sheet.write(len(group_data)+1, 0, group_key) # Write the group name
            
            # Loop over the extracted data and write to the sheet
            for i, column in enumerate(variables):
                sheet.write(len(group_data)+1, i+1, extracted_data[column].values[0])
                
    # Save the Excel file
    writer.save()

# Define the unit tests
class TestExtractDataToExcel(unittest.TestCase):
    def test_extraction(self):
        expected_output = {
            '2014-03-01': {
                'group_1': [[1, 2, 3, 4],
                            [16, 17, 18, 19],
                            [31, 32, 33, 34],
                            [46, 47, 48, 49]],
                'group_2': [[61, 62, 63, 64],
                            [76, 77, 78, 79]]
            },
            '2014-04-01': {
                'group_1': [[91, 92, 93, 94],
                            [106, 107, 108, 109],
                            [121, 122, 123, 124],
                            [136, 137, 138, 139]]
            },
            '2014-05-01': {
                'group_1': [[151, 152, 153, 154],
                            [166, 167, 168, 169]]
            }
        }
        
        extract_data_to_excel('Output.xlsx', dict_1, ['var_1', 'var_2', 'var_3', 'var_4'])
        
        # Read the extracted data from the generated file
        extracted_data = pd.read_excel('Output.xlsx', sheet_name=None)
        
        # Compare the extracted data with the expected output
        for key in expected_output:
            self.assertTrue(key in extracted_data)
            for group_key in expected_output[key]:
                self.assertTrue(group_key in extracted_data[key])
                extracted_values = extracted_data[key][group_key].values.tolist()
                self.assertEqual(extracted_values, expected_output[key][group_key])

# Run the unit tests
unittest.main(argv=[''], exit=False)