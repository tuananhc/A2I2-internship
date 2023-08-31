# To append the resulting values to your empty dataframe, you can use the `loc` method to add rows to the dataframe. You need to specify the column names and values for each row to be added. Here's how you can modify your code to append the values correctly:

# ```python
import pandas as pd

empty_df = pd.DataFrame(columns = ["date","builders","miners","roofers"])

text = "On 10 May 2022, there were 400 builders living in Rome, there were also no miners and approximately 70 roofers"
text = text.split()
profession = ["builders","miners","roofers"]

for i in text:
    if i in profession:
        row = {'date': '10 May 2022', i: text[text.index(i) - 1]}
        empty_df = empty_df.append(row, ignore_index=True)
# ```

# This code creates a dictionary `row` with keys as column names and values as the extracted values. The `ignore_index=True` parameter ensures that the index of the appended rows is updated correctly.

# To convert the 'no' or 'none' into zero, you can add a condition inside the for loop to check for such values and replace them:

# ```python
for i in text:
    if i in profession:
        value = text[text.index(i) - 1]
        if value.lower() == 'no' or value.lower() == 'none':
            value = 0
        row = {'date': '10 May 2022', i: value}
        empty_df = empty_df.append(row, ignore_index=True)
# ```

# Lastly, to incorporate the date, you can update the code to include the actual date from the text file. If you can extract it from the text file, you can replace `'10 May 2022'` with the extracted date. If the date is being updated every day, you can extract the current date in the format you want using the `datetime` module:

# ```python
import datetime

current_date = datetime.datetime.today().strftime('%d %b %Y')

for i in text:
    if i in profession:
        value = text[text.index(i) - 1]
        if value.lower() == 'no' or value.lower() == 'none':
            value = 0
        row = {'date': current_date, i: value}
        empty_df = empty_df.append(row, ignore_index=True)
# ```

# This code uses the `strftime` method to format the current date as 'day month year'. You can specify a different date format if needed.

# Hope this helps! Let me know if you have any further questions.