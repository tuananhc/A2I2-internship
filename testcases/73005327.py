```python
import unittest
import re

def myFunc(text):
    text = text.lower()
    length = len(text)
    slocid = text.index("s")
    translation = ""
    
    for letter in text:
        if (text[length-1] == "s") or (text[slocid + 1] == " "):
            translation = re.sub(r"s\b", lambda m: m.group().replace("s", "ς"), text)
        if letter == "s":
            translation = translation.replace("s", "σ")
        if letter == "a":
            translation = translation + "α"
        else:
            translation = translation + letter
            
    return translation


class MyFuncTestCase(unittest.TestCase):
    def test_translate_s_at_end_of_word(self):
        text = "as"
        expected_output = "ας"
        self.assertEqual(myFunc(text), expected_output)
        
    def test_translate_s_not_at_end_of_word(self):
        text = "sa"
        expected_output = "σα"
        self.assertEqual(myFunc(text), expected_output)
        
    def test_translate_s_in_word(self):
        text = "sakas"
        expected_output = "σαkας"
        self.assertEqual(myFunc(text), expected_output)

    def test_translate_multiple_s(self):
        text = "sassass"
        expected_output = "σασσασσ"
        self.assertEqual(myFunc(text), expected_output)
        
    def test_translate_a(self):
        text = "a"
        expected_output = "α"
        self.assertEqual(myFunc(text), expected_output)

if __name__ == "__main__":
    unittest.main()
```