import os
import re
import openai
from functools import reduce
from dotenv import load_dotenv
import json

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv('OPENAI_API_KEY')

def generateResponse(q):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{
            "role": "user", 
            "content": q["body"]
        }]
    )

    # extract the response
    message = chat_completion["choices"][0]["message"]["content"]

    filename = "./gptResponses/sub/" + q["id"] + ".py"
    f = open(filename, "w")
    f.write(message)
    f.close()

f = open("./Questions dataset/Previous internship dataset.json")
data = json.load(f)

f = open("./filteredQuestions/set3/questionset2.txt")
lines = f.readlines()

for line in lines:
    line = line.strip()
    for q in data:
        if q["id"] == line:
            generateResponse(q)