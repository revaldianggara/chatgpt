import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# ekstrak sebuah paragraf jadi beberapa nilai
# summary dari teks tersebut
# key take points dari teks tersebut
# keyword
# sentiment dari text tersebut
# aktor from the text
# jika ada event tolong sertakan tanggal berserta eventnya

load_dotenv()

openai.api_key=os.getenv('OPENAI_API_KEY')

from openai import OpenAI
client = OpenAI()

while True:
    text = input("User:")
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a text analyzer system, that will extract value from text with json format with this variables summarize: , key take points: , keyowrd: , sentiment: , actor: (a person who are involved inside the text), cronological event: (timestamp:,event:) ."},
        {"role": "user", "content": text},
    ]
    )
    print()
    print("Analyzer: ", response.choices[0].message.content)