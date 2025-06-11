import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=300
    )
    return response["choices"][0]["message"]["content"].strip()