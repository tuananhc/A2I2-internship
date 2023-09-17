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

     1. If the code is copied from a Command Line Interface, remove all the leading ">>>".
     1. Remove any duplicated code pieces.
     1. Wrap the working code inside a function called `myFunc1`. If the code is already within a function, change its name to `myFunc1`.
     1. Remove any uncommented text or typos.
     1. Import all the necessary libraries.

      Once done, we extract the code block from the answer, and write that to the file `SO_answer.py`.

3. For the GPT answer, we will supply the query with the StackOverflow question and ask GPT to wrap everything inside a function called `myFunc2`, make sure that all required libraries are imported. The answer will be written to the file `GPT_answer.py`.

4. For each question, we also generate a set of test cases with the python `unittest` library. Here are the requirements for the test suite:
   * Tests are generated from analysing the question and answer. If there are clear input and expected output from the thread, make sure that they are included with other tests as well.
   * Tests will be run on 2 functions: `myFunc1` and `myFunc2`, each require its own tests and is imported from its corresponding file.
   * All required libraries are imported.
   * Can be run straight away and require no further input.

## Prompts

As outlined, this process make heavy uses of ChatGPT as a tool to generate and normalise the data. To ensure smooth operations, it is vital that GPT answer are consistent, which is why refining the prompts used throughout the process is as important as the extraction and evaluation itself.

Some criteria that we impose on GPT's answer:

* Code blocks should be wrapped inside a \`\`\` block. GPT have a few formats of printing code (it can use `<code>` block like HTML), so enforce a type ensure the extraction process is consistent across answers. For example:
  
        ```python
          def myFunc1():
            ...
        ```

* Code should not require any further input from us, i.e. no "put your input here" and similar.
* No "..." in the code blocks. Sometimes GPT will shorten its answer by using "..." in its code output.

Below are the prompts that we used and some example:

1. Get GPT answer for StackOverflow question:

        Here's my problem: 
            
        "{query}"

        Find a solution for the problem, and put everything inside a function called "myFunc1". 
        Make sure all relevant and required libraries are imported.
        Return the output in a python code block. Make sure markdown format is used when writing code.

      The `{query}` is the StackOverflow question itself in raw form. Here's an example:

        Here's my problem: 
            
        "<p>How do I print access the entries in a Pandas Dataframe by position?</p>"

        Find a solution for the problem, and put everything inside a function called "myFunc1". 
        Make sure all relevant and required libraries are imported.
        Return the output in a python code block. Make sure markdown format is used when writing code.

## File instructions

Below are the main files needed to run the program:

* gpt.py: contain all the functions to run the query for each step above, each one contains its own prompt
  * `wrapSOCodeInAFunction()`: for step 2
  * `getGPTAnswer()`: for step 3
  * `generateTestCases()`: for step 4
* findCode.py: contain function to extract the code blocks from the StackOverflow question. This is done by finding the `<code>` tags from the question.
* extractGPTResponse.py: contain function to extract the code blocks from the GPT message. GPT will wrap code blocks between "\`\`\`" tags, so we just have to locate those tag and extract the text within.
* classifier.py: contain the code to classify the StackOverflow question into 1 of 3 categories: how-to, debug or conceptual. This is done by sending the question body to GPT along with the 3 options.

## Commands

To generate the files outlined above in [File structure](#file-structure), run:

    python3 runCodeGen.py

This will create a directory named `Code files`, with sub-directories containing each question's details:

    Code files
        └── Question_ID
        │   ├── GPT_answer.py
        │   ├── SO_answer.py
        │   ├── question.txt
        │   └── tests.py
        └── ...

## Results

Here are the results on running the test on 1000 samples:

## Limitations

The current work has many limitations. Below are some primary one that we hope to fix in the future:

* Extend the coverage to include languages other than Python. The main motivation for including just Python during this iteration is its simplicity in generating and running test cases with the `unittest` library. Additionally, many Python questions on StackOverflow revolves around data analysing and manipulation, which often comes with input and expected output.
* Extend the coverage to include other types of questions as well. For now only "how-to" kind of question are tested and used. It is feasible to test the "conceptual" questions as well based on their clarity, information density, etc.
