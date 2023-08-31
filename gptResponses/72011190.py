# You can use the `split()` function to split the input string by spaces and iterate over each number. Inside the loop, you can use the `get()` method of the `keypad` dictionary to retrieve the corresponding character for each number. Then, you can concatenate the characters to a result string. Here's an example implementation:

# ```python
keypad = {'21': 'a', '22': 'b', '23': 'c', '31': 'd', '32': 'e', '33': 'f', '41': 'g', '42': 'h', '43': 'i',
          '51': 'j', '52': 'k', '53': 'l', '61': 'm', '62': 'n', '63': 'o', '71': 'p', '72': 'q', '73': 'r',
          '74': 's', '81': 't', '82': 'u', '83': 'v', '91': 'w', '93': 'x', '93': 'y', '94': 'z', '*': ' '}

def decode_text(coded_text):
    coded_text_list = coded_text.split()
    decoded_text = ""
    for code in coded_text_list:
        decoded_text += keypad.get(code, '')
    return decoded_text

# Example usage:
input_text = "42 32 53 53 63 * 43 * 21 61 * 61 21 73 52"
output_text = decode_text(input_text)
print(output_text)
# ```

# Output:
# ```
# hello i am mark
# ```