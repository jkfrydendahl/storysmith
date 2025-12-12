from dotenv import load_dotenv
import os
import openai

#load environment variables from .env file
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

def call_openai(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-5.2",
            messages=[{"role": "user", "content": prompt}],
            temperature=1.0,
            max_completion_tokens=800
        )
        content = response["choices"][0]["message"]["content"].strip()
        if not content:
            print("Warning: Empty response from API")
        return content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        raise