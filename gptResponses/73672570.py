# Yes, you can loop over the `search_list` and find the length of each dataframe using the `len()` function. Here's an updated version of your code:

# ``` python
# Create a list to store the lengths of the dataframes
len_df = []

# Loop over the search_list
for df_name in search_list:
    # Find the length of the corresponding dataframe
    length = len(eval(df_name))
    # Create a dictionary with the dataframe name as key and length as value
    len_dict = {df_name: length}
    # Append the dictionary to the len_df list
    len_df.append(len_dict)

# Print the result
print(len_df)
# ```

# Output:
# ```
# [{'A': 2}, {'B': 4}, {'C': 1}]
# ```

# Note: Be careful when using the `eval()` function as it can execute arbitrary code. In this case, it is safe to use since the values in `search_list` are trusted and correspond to existing dataframe names.