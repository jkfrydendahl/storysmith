from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class CharacterPrompt(PromptTemplate):
    def render(self, race: str, gender: str, char_class: str, personality: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        return (
            f"Create a unique tabletop RPG character with the following parameters:\n"
            f"Race: {race}\n"
            f"Gender: {gender}\n"
            f"Class: {char_class}\n"
            f"Personality: {personality}\n"
            f"Genre/Setting: {genre}\n"
            f"Variation seed: {random_seed}\n\n"
            f"Requirements:\n"
            f"- Give them a distinctive, original name\n"
            f"- Include vivid description, memorable quirk, and clear motive\n"
            f"Do not include the variation seed number in your response."
        )

def generate_character(race: str, gender: str, char_class: str, personality: str, genre: str) -> str:
    prompt = CharacterPrompt().render(race=race, gender=gender, char_class=char_class, personality=personality, genre=genre)
    return call_openai(prompt)