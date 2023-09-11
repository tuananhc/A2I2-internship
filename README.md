# Instructions

Overview of how the evaluation process work

## Filter data

Currently only questions with "python" are evaluated. We further restrict the dataset by only consider questions about dataframes and pandas, because those question have clear input and expected output.

To extract the data, simply check if the question tags have the corresponding "python" or "dataframe" tag.

## Extract data

For each question we extract the question body, the accepted answer, the answer from ChatGPT, and we also generate unit test cases for each question.

### File structure

Each question will be in its own directory with ID as its name, and will contain the following files:

* question.txt
* GPT_answer.py
* SO_answer.py
* tests.py
* testcase.json

### Extraction process

1. The question can be written into the .txt file straight away
2. For the StackOverflow accepted answer, the answer will usually be inside a code block, which can be found with the HTML tags `<code>`. However, answer style usually differs from one another. For example, there can be multiple code blocks:

        # Solution 1

      Some text in between

        # Solution 2

      Or that an answer is displayed on the Python command line:

        >>> result = myFunc(myData)
        >>> print(result)

      To maintain a consistent format, we feed all the code blocks into GPT-4 and ask it to:

     1. Remove any duplicated code pieces.
     2. Wrap the working code inside a function called `myFunc1`. If the code is already within a function, change its name to `myFunc1`.
     3. Remove any uncommented text or typos.
     4. Import all the necessary libraries.

      Once done, we extract the code block from the answer, and write that to the file `SO_answer.py`.

3. For the GPT answer, we will supply the query with the StackOverflow question and ask GPT to wrap everything inside a function called `myFunc2`, make sure that all required libraries are imported. The answer will be written to the file `GPT_answer.py`.

4. For each question, we also generate a set of test cases with the python `unittest` library. The test file will call the 2 function `myFunc1` and `myFunc2` from `SO_answer.py` and `GPT_answer.py` respectively.

## File instructions

Below are the main files needed to run the program:

* gpt.py: contain all the functions to run the query for each step above, each one contains its own prompt
  * wrapSOCodeInAFunction: for step 2
  * getGPTAnswer(): for step 3
  * generateTestCases(): for step 4
* findCode.py: contain function to extract the code blocks from the StackOverflow question. This is done by finding the `<code>` tags from the question.
* extractGPTResponse.py: contain function to extract the code blocks from the GPT message. GPT will wrap code blocks between "\`\`\`" tags, so we just have to locate those tag and extract the text within.
* classifier.py: contain the code to classify the StackOverflow question into 1 of 3 categories: how-to, debug or conceptual. This is done by sending the question body to GPT along with the 3 options.
