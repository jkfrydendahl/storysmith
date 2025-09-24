from promts.base import PromptTemplate
from generators.openai import call_openai

class NPCPrompt(PromptTemplate):
    def render(self, race: str, gender: str, char_class: str, tone: str, genre: str) -> str:
        return (
            f"Create a tabletop RPG NPC.\n"
            f"Race: {race}\n"
            f"Gender: {gender}\n"
            f"Class: {char_class}\n"
            f"Tone: {tone}\n"
            f"Genre/Setting: {genre}\n"
            f"Requirements:\n"
            f"- Give them a distinctive, original name\n"
            f"- Include vivid description, memorable quirk, and clear motive\n"
        )

def generate_npc(race: str, gender: str, char_class: str, tone: str, genre: str) -> str:
    prompt = NPCPrompt().render(race=race, gender=gender, char_class=char_class, tone=tone, genre=genre)
    return call_openai(prompt)