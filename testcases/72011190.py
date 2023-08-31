```python
import unittest

keypad = {'21': 'a', '22': 'b', '23': 'c', '31': 'd', '32': 'e', '33': 'f', '41': 'g', '42': 'h', '43': 'i',
          '51': 'j', '52': 'k', '53': 'l', '61': 'm', '62': 'n', '63': 'o', '71': 'p', '72': 'q', '74': 'r',
          '74': 's', '81': 't', '82': 'u', '83': 'v', '91': 'w', '93': 'x', '93': 'y', '94': 'z', '*': ' '}

def myFunc(coded_string):
    normal_text = ''
    for number in coded_string.split():
        if number in keypad:
            normal_text += keypad[number]
    return normal_text

class TestMyFunc(unittest.TestCase):
    def test_no_coded_string(self):
        result = myFunc('')
        self.assertEqual(result, '')

    def test_coded_string_with_single_word(self):
        result = myFunc('42 32 53 53 63')
        self.assertEqual(result, 'hello')

    def test_coded_string_with_multiple_words(self):
        result = myFunc('42 32 53 53 63 *43 *21 61 *61 21 73 52')
        self.assertEqual(result, 'hello i am mark')

    def test_coded_string_with_unknown_number(self):
        result = myFunc('42 32 21 53 63 *43 *21 61 *61 21 73 52')
        self.assertEqual(result, 'heaio i am mark')

if __name__ == '__main__':
    unittest.main()
```