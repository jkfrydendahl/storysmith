from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class AdventurePrompt(PromptTemplate):
    def render(self, adventure_type: str, length: str, theme: str, difficulty: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        return (
            f"Create a unique tabletop RPG adventure with the following parameters:\n"
            f"Type: {adventure_type}\n"
            f"Length: {length}\n"
            f"Theme: {theme}\n"
            f"Difficulty: {difficulty}\n"
            f"Genre: {genre}\n"
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
