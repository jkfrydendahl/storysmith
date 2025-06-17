from promts.base import PromptTemplate
from generators.openai import call_openai

class NPCPrompt(PromptTemplate):
    def render(self, race: str, char_class: str, tone: str, genre: str) -> str:
        return (
            f"Create a tabletop RPG NPC.\n"
            f"Race: {race}\n"
            f"Class: {char_class}\n"
            f"Tone: {tone}\n"
            f"Genre/Setting: {genre}\n"
            f"Include name, description, quirk, and motive."
        )

def generate_npc(race: str, char_class: str, tone: str, genre: str) -> str:
    prompt = NPCPrompt().render(race=race, char_class=char_class, tone=tone, genre=genre)
    return call_openai(prompt)