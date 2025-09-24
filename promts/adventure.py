from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class AdventurePrompt(PromptTemplate):
    def render(self, adventure_type: str, length: str, theme: str, difficulty: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        
        # Handle empty parameters by using descriptive language
        type_param = adventure_type if adventure_type.strip() and adventure_type.strip().lower() != "undefined" else "engaging adventure"
        length_param = length if length.strip() and length.strip().lower() != "undefined" else "suitable length"
        theme_param = theme if theme.strip() and theme.strip().lower() != "undefined" else "compelling theme"
        difficulty_param = difficulty if difficulty.strip() and difficulty.strip().lower() != "undefined" else "balanced difficulty"
        genre_param = genre if genre.strip() and genre.strip().lower() != "undefined" else "fantasy setting"
        
        return (
            f"Create a unique tabletop RPG adventure with the following parameters:\n"
            f"Type: {type_param}\n"
            f"Length: {length_param}\n"
            f"Theme: {theme_param}\n"
            f"Difficulty: {difficulty_param}\n"
            f"Genre: {genre_param}\n"
            f"Variation seed: {random_seed}\n\n"
            f"Format your response with clear headings:\n\n"
            f"Title: [Give it an engaging, memorable title]\n\n"
            f"Hook: [The initial situation or call to action that draws the party in]\n\n"
            f"Background: [The underlying situation, history, or conflict driving the adventure]\n\n"
            f"Key Locations: [2-4 important places the adventure takes place, with brief descriptions]\n\n"
            f"Important NPCs: [Key characters the party will interact with, including their motivations]\n\n"
            f"Main Challenges: [Primary obstacles, encounters, or puzzles the party must overcome]\n\n"
            f"Potential Rewards: [Treasure, information, allies, or other benefits for success]\n\n"
            f"Complications: [Possible twists, moral dilemmas, or unexpected developments]\n\n"
            f"Resolution Options: [Multiple ways the adventure could conclude based on party actions]\n\n"
            f"Do not include the variation seed number in your response."
        )

def generate_adventure(adventure_type: str, length: str, theme: str, difficulty: str, genre: str) -> str:
    prompt = AdventurePrompt().render(adventure_type=adventure_type, length=length, theme=theme, difficulty=difficulty, genre=genre)
    return call_openai(prompt)
