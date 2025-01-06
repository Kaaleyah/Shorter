from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

with open("transcription_with_timestamps.txt", "r") as file:
    transcription = file.read()


client = OpenAI(
    api_key=OPENAI_KEY
)

callToChat = client.chat.completions.create(
    model="gpt-4o-mini",
    store=False,
    messages=[
        {"role": "user", "content": f"Here is a transcript of a video podcast. I want you to extract the most compelling and interesting parts. These parts will be used to make clips. These clips should be 60 seconds. Please provide me timestamps for these clips. {transcription}"}
    ]
)

response = callToChat.choices[0].message.content
print(response)