# To make sure the file is saved in the new subfolder, you should update the `openFile()` function as follows:

# ``` python
def openFile():
    filename = filedialog.askopenfilename(initialdir = r'L:\folder\My_file', filetypes=[("Excel Files", "*.xlsx")])
    os.startfile(filename)
    df = pd.read_excel(filename, sheet_name='Order Details')
    
    # Specify the full path to the new file in the subfolder
    new_file_path = os.path.join(os.path.join(path.get(), folder.get()), 'Intelliscan.xlsx')
    
    # Save the modified df as a new excel file in the subfolder
    df.to_excel(new_file_path, index=False)
# ```

# This code uses the `os.path.join()` function to concatenate the path of the selected directory (`path.get()`) with the name of the new subfolder (`folder.get()`) and adds the final file name (`Intelliscan.xlsx`) to create the complete path to the new file. The modified DataFrame is then saved using this new file path.