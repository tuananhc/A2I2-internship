import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv('OPENAI_API_KEY')

def getGPTAnswer(query): 
  chat_completion = openai.ChatCompletion.create(
    model="gpt-4", 
    messages=[{
      "role": "user", 
      "content": f"""
        Here's my problem: 
        
        {query}

        Find a solution for the problem, and put everything inside a function called "myFunc1". 
        Make sure all relevant and required libraries are imported.
      """
    }]
  )

  return chat_completion["choices"][0]["message"]["content"]

def getInputOutput(query):
  chat_completion = openai.ChatCompletion.create(
    model="gpt-4", 
    messages=[{
      "role": "user", 
      "content": f"""
        From this thread, find the expected input and output of the problem and put them in a JSON object with 2 keys "input" and "output.

        ```{query}```

        Answer with a JSON block code.
      """
    }]
  )

  return chat_completion["choices"][0]["message"]["content"]

def wrapSOCodeInAFunction(code):
  chat_completion = openai.ChatCompletion.create(
    model="gpt-4", 
    messages=[{
      "role": "user", 
      "content": f"""
        Wrap this code piece in a function called `myFunc2`, if it is already wrapped, change the name of the function to `myFunc2`. 
        Import all the necessary libraries. 
        There can be duplicated code pieces, remove them.
        There can be uncommented text, find and remove them form the function.
        Here's the code:

        ```
        {code}
        ```
      """
    }]
  )

  return chat_completion["choices"][0]["message"]["content"]

def gptQuery(query):
  chat_completion = openai.ChatCompletion.create(
    model="gpt-4", 
    messages=[{
      "role": "user", 
      "content": query
    }]
  )

  return chat_completion["choices"][0]["message"]["content"]

def generateTestCases(q):
  query = f"""Generate python unit test cases similar to the unittest library for this task: 
      {q["body"]}.
      The test will be run on 2 functions, myFunc1 and myFunc2. `myFunc1` will be imported from 'gpt_code_answer.py' and 'myFunc2' will be imported from 'SO_answer.py'.
      If DataFrames are being compared, ignore their indexes.
      Nest the returning result in a Python code block.
    """
  chat_completion = openai.ChatCompletion.create(
    model="gpt-4", 
    messages=[{
      "role": "user", 
      "content": query
    }]
  )

  # extract the response
  message = chat_completion["choices"][0]["message"]["content"]
  print(message)
  return message

question = ""
code = ""
prompt = f"""
  Here's a problem that I have:

  {question}

  Here's the program that I come up with:
  ```python
    {code}
  ```

  Wrap this code piece in a function called `myFunc2`, if it is already wrapped, change the name of the function to `myFunc2`. 
  Import all the necessary libraries. 
  There can be duplicated code pieces, or sections that serve the same purpose, remove the duplicates.
  If there are multiple solutions presented within the code, save only the first one.
  There can be uncommented text, find and remove them form the function.
"""