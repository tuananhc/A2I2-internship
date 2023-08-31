Here are some unit test cases for the 'myFunc' function:

1. Test case when the csv file has only one value:
    - Input: csv file with values [1]
    - Expected output: csv file with values [1, 0]

2. Test case when the csv file has multiple values:
    - Input: csv file with values [1, 9, 5, 7, 3]
    - Expected output: csv file with values [1, 8, 3, 4, -4]

3. Test case when the csv file has negative values:
    - Input: csv file with values [-1, -5, -3]
    - Expected output: csv file with values [-1, -4, 2]

4. Test case when the csv file has repetitive values:
    - Input: csv file with values [1, 1, 1, 1]
    - Expected output: csv file with values [1, 0, 0, 0]

5. Test case when the csv file has alphanumeric values:
    - Input: csv file with values [a, 1, b, 2, c]
    - Expected output: csv file with values [a, 0, b, 1, -1]

6. Test case when the csv file has empty values:
    - Input: csv file with values [ , , , ]
    - Expected output: csv file with values [ , , , , 0]

Note: These test cases assume that the 'myFunc' function takes the csv file as an argument and modifies it in-place by adding the computed differences in the second column.