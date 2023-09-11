import json
import openai
import os
from dotenv import load_dotenv

from filterQuestions import *
from findCode import *
from gpt import gptQuery
from findCode import findCode


def classifyAll():
    load_dotenv()

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv('OPENAI_API_KEY')

    f = open("./Questions dataset/Previous internship dataset.json")
    data = json.load(f)
    header = ["num", "question_id"]

    for q in data:
        if len(q["body"]) > 3800: # avoid reaching maximum GPT query length
            continue
        query = "Classify this question into one of these three categories: debugging, how-to or conceptual: \"" + q["body"] + "\". Answer with the chosen category only."
        response = gptQuery(query)
        if response == "how-to":
            if "python" in q["tags"]:
                if (not filterImage(q["body"]) and not filterImage(q["body_1"])):
                    print(q["id"])
                    print(findCode(q["body"]))

def classify(question):
    query = "Classify this question into one of these three categories: debugging, how-to or conceptual: \"" + question + "\". Answer with the chosen category only."
    response = gptQuery(query)
    return response