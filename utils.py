import html
import re
from typing import List
from functools import reduce
from dotenv import load_dotenv

load_dotenv()

def findCode(text: str) -> str:
    sub1 = "\u003ccode\u003e"
    sub2 = "\u003c/code\u003e"

    occurrences1 = re.finditer(sub1, text)
    
    res1 = reduce(lambda x, y: x + [y.start()], occurrences1, [])

    occurrences2 = re.finditer(sub2, text)
    
    res2 = reduce(lambda x, y: x + [y.start()], occurrences2, [])

    res = ""
    
    for index in range(len(list(res1))):
        code = text[res1[index] + 6 : res2[index]]

        # The \n find is for finding code blocks only and ignore inline code
        if code.find("\n") == -1:
            continue

        res += code + '\n'

    return html.unescape(res)

def extractCodeFromGPTAnswer(answer: str) -> str:
    # the code is nested in a ``` block just as a DOCTYPE would, so we are finding 
    # the indexes of the ``` segments within the answer, to retrieve the code within
    sub = "```"
    occurrences1 = re.finditer(sub, answer)
    
    res = reduce(lambda x, y: x + [y.start()], occurrences1, [])

    start = answer[res[0]:].find('\n')

    return answer[res[0] + start + 1: res[1]]

def removeCLIPrompt(code: str) -> str:
    code = re.sub(r"^(>>>)", " ", code)
    return code

def extract_code(text: str) -> str:
    return "\n\n".join(extract_all_code(text))

def extract_all_code(text: str) -> List[str]:
    pattern = r"```(?:python)?\n(.+?)```"
    if re.search(pattern, text, flags=re.DOTALL):
        return re.findall(pattern, text, flags=re.DOTALL)
    return [text]
