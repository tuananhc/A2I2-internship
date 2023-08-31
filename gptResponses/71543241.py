# You can use a dictionary to store the sum and count of values for each year. Then, calculate the average by dividing the sum by the count. Here's an example solution:

# ```python
data = [
    ['425842', '2008', 'Monday', '23:30:00', '10'],
    ['425843', '2008', 'Tuesday', '23:30:00', '9'],
    ['425844', '2009', 'Monday', '23:30:00', '2'],
    ['425845', '2009', 'Monday', '23:30:00', '3'],
    ['425846', '2010', 'Monday', '23:30:00', '2'],
    ['425847', '2010', 'Monday', '23:30:00', '10'],
    ['425848', '2010', 'Tuesday', '23:30:00', '10']
]

averages = {}  # Dictionary to store sum and count for each year

for row in data:
    year = row[1]
    value = float(row[4])
    
    if year in averages:
        averages[year][0] += value  # Add value to sum
        averages[year][1] += 1  # Increment count
    else:
        averages[year] = [value, 1]  # Initialize sum and count
        
# Calculate averages
result = [[year, round(averages[year][0] / averages[year][1], 2)] for year in averages]

# Sort by year
result.sort(key=lambda x: x[0])

# Print averages
for year, avg in result:
    print([year, avg])
# ```

# This will give you the desired output:

# ```python
# [2008, 9.5]
# [2009, 2.5]
# [2010, 7.33]
# ```

# Note that the values ​​in the last column are converted to float before calculating the average, assuming they are numerical values.