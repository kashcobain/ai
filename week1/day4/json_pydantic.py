import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    phone_number:int
schema=Ticket.model_json_schema()
response_format={"type": "json_object", "schema": schema}
system_prompt=f"""You are a customer support agent. You will be given a customer ticket. Your task is to extract personal information from the ticket based on this schema {schema} and give me an json object as output. If you are unable to extract any personal information, return an empty json object. Do not give any explanation or text other than the json object. """
message_system={
    "role": "system",
    "content": system_prompt
}
client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
text="hello my name is karan, i purchased an iphone, my number is 8791662011, my email is abc@gmail.com. kindly look intyo the matter"
prompt=f"""this is a customer ticket. please extract personal information from this {text} """

# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages,response_format=response_format)


answer=response.choices[0].message.content
print(answer)
# isko padhte kaise hain
import json
raw_json=answer
data_file= json.loads(raw_json)
ticket=Ticket(**data_file)
print(ticket.name)


























