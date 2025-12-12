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

def remove_unwanted_endings(text: str) -> str:
    """Remove helpful but unwanted follow-up offers from the model"""
    # Patterns that indicate the model is offering additional content
    unwanted_patterns = [
        r'\n\n.*?[Ii]f you[\'d]* like.*',
        r'\n\n.*?[Ww]ould you like.*',
        r'\n\n.*?[Ll]et me know if.*',
        r'\n\n.*?[Ff]eel free to.*',
        r'\n\n.*?[Ii] can (?:add|provide|create|generate).*',
    ]
    
    for pattern in unwanted_patterns:
        text = re.sub(pattern, '', text, flags=re.DOTALL)
    
    return text.strip()

def call_openai(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-5.2",
            messages=[{"role": "user", "content": prompt}],
            temperature=1.0,
            max_completion_tokens=1200
        )
        
        # Check if the response was truncated due to token limit
        finish_reason = response["choices"][0].get("finish_reason")
        if finish_reason == "length":
            print("Warning: Response was truncated due to token limit. Consider increasing max_completion_tokens.")
        
        content = response["choices"][0]["message"]["content"].strip()
        if not content:
            print("Warning: Empty response from API")
            return content
        
        # Strip markdown formatting
        content = strip_markdown(content)
        
        # Remove unwanted follow-up offers
        content = remove_unwanted_endings(content)
        
        return content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        raise