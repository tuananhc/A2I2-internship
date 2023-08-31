import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv('OPENAI_API_KEY')

def gptQuery(query): 

    chat_completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{
            "role": "user", 
            "content": query
        }]
    )

    return chat_completion["choices"][0]["message"]["content"]