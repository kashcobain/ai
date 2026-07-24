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
# 3 prompts
prompt1="hi"
prompt2="write a essay on ai"
prompt3="explain timme travel in detail"

# message me role and content
prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:

    message={
        "role": role,
        "content": prompt
    }

    messages=[message]

    response=client.chat.completions.create(model=model, messages=messages,max_tokens=100)
    usage=response.usage
    print(f"Prompt: {prompt}--->completion tokens used: {usage.completion_tokens}, prompt tokens used: {usage.prompt_tokens}, total tokens used: {usage.total_tokens} ,finish reason: {response.choices[0].finish_reason}   ")   
# print(response)

# print("#######################################")

# answer=response.choices[0].message.content
# print(answer)