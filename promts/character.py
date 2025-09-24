from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class CharacterPrompt(PromptTemplate):
    def render(self, race: str, gender: str, char_class: str, personality: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        
        # Handle empty parameters by using descriptive language
        race_param = race if race.strip() and race.strip().lower() != "undefined" else "random race"
        gender_param = gender if gender.strip() and gender.strip().lower() != "undefined" else "any gender"
        class_param = char_class if char_class.strip() and char_class.strip().lower() != "undefined" else "suitable class"
        personality_param = personality if personality.strip() and personality.strip().lower() != "undefined" else "unique personality"
        genre_param = genre if genre.strip() and genre.strip().lower() != "undefined" else "fantasy setting"
        
        return (
            f"Create a unique tabletop RPG character with the following parameters:\n"
            f"Race: {race_param}\n"
            f"Gender: {gender_param}\n"
            f"Class: {class_param}\n"
            f"Personality: {personality_param}\n"
            f"Genre/Setting: {genre_param}\n"
            f"Variation seed: {random_seed}\n\n"
            f"Requirements:\n"
            f"- Give them a distinctive, original name\n"
            f"- Include vivid description, memorable quirk, and clear motive\n"
            f"Do not include the variation seed number in your response."
        )

def generate_character(race: str, gender: str, char_class: str, personality: str, genre: str) -> str:
    prompt = CharacterPrompt().render(race=race, gender=gender, char_class=char_class, personality=personality, genre=genre)
    return call_openai(prompt)