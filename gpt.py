import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv('OPENAI_API_KEY')

# only for generating the answer will we use GPT-4 to speed up the process
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
                Return the output in a python code block. Make sure markdown format is used when writing code.
            """
        }]
    )

    return chat_completion["choices"][0]["message"]["content"]

def getInputOutput(query):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
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
        model="gpt-3.5-turbo", 
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
        model="gpt-3.5-turbo", 
        messages=[{
            "role": "user", 
            "content": query
        }]
    )

    return chat_completion["choices"][0]["message"]["content"]

def generateTestCases(q):
    query = f"""Consider this problem: 

        "{q["body"]}"

        This is my work on the problem: 

        "{q["body_1"]}"

        From these 2 segments, generate Python unittest for the problem. 
        The test will be run on 2 functions, myFunc1 and myFunc2. `myFunc1` will be imported from 'GPT_answer.py' and 'myFunc2' will be imported from 'SO_answer.py'. Each function will need its own test. 
        Nest the returning result in a Python code block. 
        If there are specific input and expected output presented in the threads above, include them with the tests generated above as well.
        If DataFrames comparison is involved, do not compare the DataFrames' index.
        Import all the required and up-to-date libraries.
        All the tests should be concrete, can be run straight away and require no further input.
    """
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{
            "role": "user", 
            "content": query
        }]
    )

    # extract the response
    message = chat_completion["choices"][0]["message"]["content"]
    return message

def classifyQuestion(q):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{
            "role": "user", 
            "content": f"""
                Classify this question into one of three categories: how-to, debug, or conceptual:

                {q["body"]}

                Give the answer as JSON with the key "category".
            """
        }]
    )

    return chat_completion["choices"][0]["message"]["content"]

def cleanUpTestCode(testCode):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{
            "role": "user", 
            "content": f"""This python unittest code has some errors and possibly missing statements, find if there are any format errors or syntax errors, and add in details where needed: 
                ```
                {testCode}
                ```
                Ensure at the end of the program there is a main module declaration.
                If the program make use of pandas.testing.assert_frame_equal to compare DataFrames, replace them with numpy.array_equal instead. 
                Return the entire program in a Python block code with .md format.
            """
        }]
    )

    return chat_completion["choices"][0]["message"]["content"]
    
# question = ""
# code = ""
# prompt = f"""
# Here's a problem that I have:

# {question}

# Here's the program that I come up with:
# ```python
#     {code}
# ```

# Wrap this code piece in a function called `myFunc2`, if it is already wrapped, change the name of the function to `myFunc2`. 
# Import all the necessary libraries. 
# There can be duplicated code pieces, or sections that serve the same purpose, remove the duplicates.
# If there are multiple solutions presented within the code, save only the first one.
# There can be uncommented text, find and remove them form the function.
# Make sure all the required libraries are imported.

# """

# Return only the code in the completion. I don't want any other comments. Don't say "here is your code" or similar remarks.