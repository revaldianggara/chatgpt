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
        {"role": "system", "content": "You are a seniment analyzer system, please output positif, negatif, or neutral on every input i gave."},
        {"role": "user", "content": text},
    ]
    )
    print()
    print("Sentiment: ", response.choices[0].message.content)