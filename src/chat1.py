import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(
base_url=os.environ["LLM_BASE_URL"],
api_key=os.environ["LLM_API_KEY"],
)
r = client.chat.completions.create(
model=os.environ["LLM_MODEL"],
temperature=0.7,
messages=[{"role": "user",
"content": "用一句話解釋什麼是 AI agent harness"}],
)
print(r.choices[0].message.content)
print(r.usage)