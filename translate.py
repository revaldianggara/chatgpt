import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key=os.getenv('OPENAI_API_KEY')

from openai import OpenAI
client = OpenAI()

while True:
    text = input("User:")
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a translator system  with input Bahasa Indonesia and output is Spanish."},
        {"role": "user", "content": "translate this" + text},
    ]
    )

    print("Translator: ", response.choices[0].message.content)