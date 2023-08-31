# ```python
import spacy
from spacy.matcher import Matcher

def myFunc(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    
    matcher = Matcher(nlp.vocab)
    pattern = [
        {"OP": "*"},
        {"POS": "ADJ"},
        {"IS_PUNCT": True},
        {"POS": "ADJ"},
        {"OP": "*"},
        {"POS": "CCONJ"},
        {"OP": "*"},
        {"POS": "ADJ"}
    ]
    matcher.add("AdjList", [pattern])
    
    matches = matcher(doc)
    result = [doc[start:end].text for _, start, end in matches]
    return result

# Unit tests
def test_myFunc():
    # Test case 1
    text1 = "She told me that her dog was big, black and strong."
    expected_output1 = ["big, black and strong"]
    assert myFunc(text1) == expected_output1
    
    # Test case 2
    text2 = "She told me that her dog was big and black."
    expected_output2 = ["big and black"]
    assert myFunc(text2) == expected_output2
    
    # Test case 3
    text3 = "She told me that her dog was big, black, strong and playful."
    expected_output3 = ["big, black, strong and playful"]
    assert myFunc(text3) == expected_output3
    
    # Test case 4
    text4 = "She told me that her dog was big."
    expected_output4 = []
    assert myFunc(text4) == expected_output4
    
    # Test case 5
    text5 = "She told me that her dog was."
    expected_output5 = []
    assert myFunc(text5) == expected_output5
    
    # Test case 6
    text6 = ""
    expected_output6 = []
    assert myFunc(text6) == expected_output6
    
    # Test case 7
    text7 = "She told me that her dog was big, black, and strong but also playful."
    expected_output7 = ["big, black, and strong", "strong but also playful"]
    assert myFunc(text7) == expected_output7
    
    print("All test cases pass")

test_myFunc()
# ```