import html
import json
import openai
import os
import re
from dotenv import load_dotenv

from filterQuestions import *
from findCode import *
from gpt import *
from extractCodeFromGPTResponse import *
from classifier import classify

load_dotenv()

def createPrompt(body):
    prompt = f"""
        Which coding language is this code fragment written in? Answer in JSON form with 2 keys: "language" and "extension", if no language is detected, return "NA" for both fields:
        ```
            {body}
        ```
    """
    return prompt

def removeCLIPrompt(code):
    code = re.sub(r"^(>>>)", " ", code)
    return code

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv('OPENAI_API_KEY')

f = open("./Questions dataset/Previous internship dataset.json")
data = json.load(f)
header = ["num", "question_id"]

parentDir = "./Test Environment/resultS"
count = 0
for q in data:
	if "python" in q["tags"] and ("pandas" in q["tags"] or "dataframe" in q["tags"]):	
		if len(q["body"]) > 3800:
			continue

		# questionType = classify(q["body"])
		# if questionType != "how-to":
		# 	continue
		
		newDir = q["id"]
		path = os.path.join(parentDir, newDir)
		os.mkdir(path)

		with open(path + "/" + "question.txt", "w") as f:
			f.write(html.unescape(q["body"]))

		# extract the code pieces from the SO answer
		code = findCode(q["body_1"])
		code = removeCLIPrompt(code)
		code = wrapSOCodeInAFunction(code)
		code = extractCodeFromGPTAnswer(code)
		with open(path + "/SO_answer.py", "w")as f:
			f.write(code)

		testCase = getInputOutput(q["body"])
		print(testCase)
		with open(path + "/testcase.json", "w")as f:
			try:
				testCase = extractCodeFromGPTAnswer(testCase)
			except IndexError:
				pass
			testCase = json.loads(testCase)
			json.dump(testCase, f)

		gptAnswer = getGPTAnswer(q["body"])
		with open(path + "/GPT_answer.txt", "w") as f:
			f.write(gptAnswer)

		unitTestCases = generateTestCases(q)
		unitTestCases = extractCodeFromGPTAnswer(unitTestCases)
		with open(path + "/tests.py", "w") as f:
			f.write(unitTestCases)
		
		try:
			code = extractCodeFromGPTAnswer(gptAnswer)
			with open(path + "/gpt_code_answer.py", "w") as f:
				f.write(code)
		except IndexError:
			print('lmao')
		count += 1
		if count > 10:
			break

print("DONE")