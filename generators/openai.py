from dotenv import load_dotenv
import os
import openai
import re

#load environment variables from .env file
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

def strip_markdown(text: str) -> str:
    """Remove common markdown formatting from text"""
    # Remove headers (## Header)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove bold (**text** or __text__)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'__(.+?)__', r'\1', text)
    # Remove italic (*text* or _text_)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'_(.+?)_', r'\1', text)
    # Remove bullet points (- or * at start of line)
    text = re.sub(r'^\s*[-*]\s+', '', text, flags=re.MULTILINE)
    # Remove inline code (`code`)
    text = re.sub(r'`(.+?)`', r'\1', text)
    return text

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
        # Strip markdown formatting before returning
        content = strip_markdown(content)
        return content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        raise