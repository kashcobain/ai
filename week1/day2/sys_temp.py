import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="suggest some desi food deliuevry app name"
# message me role and content
message_system={
    "role": "system",
    "content": "You are my brand manager susggest some good name for fooddelivery app"
}   
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]
# temperature daldo ab default 0
response=client.chat.completions.create(model=model, messages=messages, temperature=1.5)
print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)