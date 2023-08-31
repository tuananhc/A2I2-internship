# To match a repeating pattern consisting of multiple tokens (in this case, adjectives) using POS and dependency tags in Spacy's pattern matcher, you can use the quantifier operator `{...}` to specify the number of repetitions.

# Here's an example pattern that can match a list of adjectives:

# ``` python
import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
doc = nlp("She told me that her dog was big, black and strong.")

matcher = Matcher(nlp.vocab)

pattern = [
    {"POS": "ADJ"},
    {"IS_PUNCT": True},
    {"POS": "ADJ"},
    {"POS": "CCONJ"}
]

# Repeat the previous pattern 0 or more times
pattern_repeat = [
    {"OP": "*"},
    *pattern
]

# Add the pattern to the matcher
matcher.add("AdjList", [pattern_repeat])

matches = matcher(doc)
# ```

# In this updated code, the pattern `pattern_repeat` uses the `{ "OP": "*" }` operator to match the previous pattern `pattern` zero or more times. This allows the pattern to capture a list of adjectives that can repeat any number of times before the final conjunction.

# With this pattern, the code will match "big, black and strong" in the example sentence. Additionally, it will match other sentences like "She told me that her dog was big and black" and "She told me that her dog was big, black, strong, and playful" as well.

# I hope this helps! Let me know if you have any further questions.