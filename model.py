from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("API_KEY")
client = OpenAI()

response = client.response.create(model="gpt-6-astra", input="Write a short bedtime story about a unicorn.")

print(response.output_text) 


