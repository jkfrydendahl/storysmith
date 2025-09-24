from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class LocationPrompt(PromptTemplate):
    def render(self, location_type: str, size: str, setting: str, tone: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        return (
            f"Create a unique tabletop RPG location with the following parameters:\n"
            f"Location Type: {location_type}\n"
            f"Size: {size}\n"
            f"Setting: {setting}\n"
            f"Atmosphere/Condition: {tone}\n"
            f"Genre: {genre}\n"
            f"Variation seed: {random_seed}\n\n"
            f"Format your response with clear headings:\n\n"
            f"Name: [Give it a distinctive, memorable name]\n\n"
            f"Description: [Vivid description of appearance and atmosphere]\n\n"
            f"Notable Features: [Key features, inhabitants, or hazards]\n\n"
            f"Details: [Interesting details that make it feel unique and lived-in]\n\n"
            f"History and Secrets: [Any relevant backstory or hidden elements]\n\n"
            f"Do not include the variation seed number in your response."
        )

def generate_location(location_type: str, size: str, setting: str, tone: str, genre: str) -> str:
    prompt = LocationPrompt().render(location_type=location_type, size=size, setting=setting, tone=tone, genre=genre)
    return call_openai(prompt)
