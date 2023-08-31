# To achieve your desired output, you can modify your code as follows:

# ```python
import pandas as pd
import numpy as np

def calculate_file():
    # Create an Excel Writer object
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    
    for i in range(40):
        # This is a toy dataframe
        random_data = np.random.randint(10,25,size=(5,3))
        df = pd.DataFrame(random_data, columns=['Column_1','Column_2','Column_3'])
        
        # Write the dataframe to a sheet with name 'Sheet_i+1'
        df.to_excel(writer, sheet_name='Sheet{}'.format(i+1), index=False)
    
    # Save the Excel file
    writer.save()
    
calculate_file()
# ```

# In this code, I have made the following changes:

# 1. Create an Excel writer object using `pd.ExcelWriter()` with the output file name and the desired engine (in this case, 'xlsxwriter').

# 2. Inside the loop, use `df.to_excel()` to write the dataframe to an Excel sheet with the desired sheet name. I have used the format 'Sheet{}'.format(i+1) to create the sheet names 'Sheet1' to 'Sheet40'.

# 3. After the loop, call `writer.save()` to save the Excel file with all the dataframes in separate sheets.

# Now, when you run this code, it will create a file named 'output.xlsx' with 40 sheets, each containing a separate dataframe.