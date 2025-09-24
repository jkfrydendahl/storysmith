from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class LocationPrompt(PromptTemplate):
    def render(self, location_type: str, size: str, setting: str, tone: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        
        # Handle empty parameters by using descriptive language
        type_param = location_type if location_type.strip() and location_type.strip().lower() != "undefined" else "interesting location"
        size_param = size if size.strip() and size.strip().lower() != "undefined" else "appropriate size"
        setting_param = setting if setting.strip() and setting.strip().lower() != "undefined" else "suitable setting"
        tone_param = tone if tone.strip() and tone.strip().lower() != "undefined" else "atmospheric mood"
        genre_param = genre if genre.strip() and genre.strip().lower() != "undefined" else "fantasy setting"
        
        return (
            f"Create a unique tabletop RPG location with the following parameters:\n"
            f"Location Type: {type_param}\n"
            f"Size: {size_param}\n"
            f"Setting: {setting_param}\n"
            f"Atmosphere/Condition: {tone_param}\n"
            f"Genre: {genre_param}\n"
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
