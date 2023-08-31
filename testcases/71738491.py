```python
import unittest
from unittest.mock import patch

def myFunc():
    embed_title_1 = ":spy: look it's a spy"
    embed_title_2 = ":YellowCred: This is a yellow cred"

    embed1 = discord.Embed(title=embed_title_1)
    embed2 = discord.Embed(title=embed_title_2)

    return embed1, embed2

class MyFuncTestCase(unittest.TestCase):
    def test_valid_emoji(self):
        expected_title_1 = ":spy: look it's a spy"
        expected_title_2 = ":YellowCred: This is a yellow cred"
        
        embed1, embed2 = myFunc()
        
        self.assertEqual(embed1.title, expected_title_1)
        self.assertEqual(embed2.title, expected_title_2)
    
    def test_invalid_emoji(self):
        expected_title = ":YellowCred: This is a yellow cred"
        with patch("discord.Embed") as MockEmbed:
            MockEmbed.return_value = MockEmbed
            MockEmbed.title = expected_title
            
            embed1, embed2 = myFunc()

            self.assertEqual(embed1.title, expected_title)
            self.assertEqual(embed2.title, expected_title)

if __name__ == '__main__':
    unittest.main()
```

Explanation:
- We import the necessary modules: `unittest` for creating test cases, and `patch` from `unittest.mock` for mocking the `discord.Embed` class.
- We define the function `myFunc()` which internally creates two `discord.Embed` objects with different titles.
- We define a test case class `MyFuncTestCase` that inherits from `unittest.TestCase`.
- Inside the `MyFuncTestCase` class, we define two test methods:
  - `test_valid_emoji()`: This test case checks if the titles of the embeds created by `myFunc()` match the expected titles for valid emojis.
  - `test_invalid_emoji()`: This test case mocks the `discord.Embed` class and assigns a custom title. It then checks if the titles of the embeds created by `myFunc()` match the assigned custom title.
- Finally, we run the tests by calling `unittest.main()`.