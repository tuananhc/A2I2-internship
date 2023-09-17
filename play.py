import html
import json
import openai
import os
import re
from tqdm import tqdm
from dotenv import load_dotenv

from utils import *
from gpt import *

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv('OPENAI_API_KEY')

f = open("./Questions dataset/Previous internship dataset.json")
data = json.load(f)

parentDir = os.getenv("DIR")

for i in tqdm(range(len(data))):
	q = data[i]
	if "python" in q["tags"]:	
		if len(q["body"]) > 3800:
			continue

		newDir = q["id"]
		path = os.path.join(parentDir, newDir)
		if (os.path.exists(path)):
			continue
		os.mkdir(path)

		questionType = classifyQuestion(q)
		print(questionType)
		questionType = json.loads(questionType)
		if questionType["category"] != "how-to":
			continue

		with open(path + "/" + "question.txt", "w") as f:
			f.write(html.unescape(q["body"]))

		# extract the code pieces from the SO answer
		code = findCode(q["body_1"])
		code = removeCLIPrompt(code)
		code = wrapSOCodeInAFunction(code)

		try:
			code = extractCodeFromGPTAnswer(code)
			with open(path + "/SO_answer.py", "w") as f:
				f.write(code)
		except IndexError:
			with open(path + "/SO_answer.txt", "w") as f:
				f.write(code)

		gptAnswer = getGPTAnswer(q["body"])
		with open(path + "/GPT_answer.txt", "w") as f:
			f.write(gptAnswer)

		unitTestCases = generateTestCases(q)
		print(unitTestCases)
		unitTestCases = extractCodeFromGPTAnswer(unitTestCases)
		cleanTestCase = cleanUpTestCode(unitTestCases)
		cleanTestCase = extractCodeFromGPTAnswer(cleanTestCase)
		with open(path + "/tests.py", "w") as f:
			f.write(cleanTestCase)
		
		try:
			code = extractCodeFromGPTAnswer(gptAnswer)
			with open(path + "/GPT_answer.py", "w") as f:
				f.write(code)
		except IndexError:
			pass

print("DONE")