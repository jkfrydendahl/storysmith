from storysmith.prompts.base import PromptTemplate
from storysmith.generators.openai import call_openai

class NPCPrompt(PromptTemplate):
    def render(self, race: str, char_class: str, tone: str) -> str:
        return (
            f"Create a tabletop RPG NPC.\n"
            f"Race: {race}\n"
            f"Class: {char_class}\n"
            f"Tone: {tone}\n"
            f"Include name, description, quirk, and motive."
        )

def generate_npc(race: str, char_class: str, tone: str) -> str:
    prompt = NPCPrompt().render(race=race, char_class=char_class, tone=tone)
    return call_openai(prompt)