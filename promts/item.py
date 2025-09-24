from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class ItemPrompt(PromptTemplate):
    def render(self, item_type: str, rarity: str, material: str, style: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        
        # Handle empty parameters by using descriptive language
        type_param = item_type if item_type.strip() and item_type.strip().lower() != "undefined" else "useful item"
        rarity_param = rarity if rarity.strip() and rarity.strip().lower() != "undefined" else "appropriate rarity"
        material_param = material if material.strip() and material.strip().lower() != "undefined" else "suitable material"
        style_param = style if style.strip() and style.strip().lower() != "undefined" else "distinctive style"
        genre_param = genre if genre.strip() and genre.strip().lower() != "undefined" else "fantasy setting"
        
        return (
            f"Create a unique tabletop RPG item with the following parameters:\n"
            f"Item Type: {type_param}\n"
            f"Rarity: {rarity_param}\n"
            f"Material: {material_param}\n"
            f"Style: {style_param}\n"
            f"Genre: {genre_param}\n"
            f"Variation seed: {random_seed}\n\n"
            f"Format your response with clear headings:\n\n"
            f"Name: [Give it a distinctive, memorable name]\n\n"
            f"Description: [Vivid description of appearance and craftsmanship]\n\n"
            f"Properties: [Mechanical effects, magical properties, or special abilities]\n\n"
            f"Details: [Interesting lore, creation story, or unique characteristics]\n\n"
            f"History: [Background, previous owners, or legendary tales if appropriate]\n\n"
            f"Game Statistics (Suggestion): [Provide appropriate RPG stats based on item type, rarity and properties:\n"
            f"- Weapons: weapon type, damage and damage type, reach, properties, weight, value\n"
            f"- Armor: AC bonus, armor type, special properties, weight, value\n"
            f"- Potions: effects, duration, usage restrictions, value\n"
            f"- Tools: skill bonuses, special abilities, weight, value\n"
            f"- Artifacts: magical properties, attunement(or similar stat), charges/uses, rarity effects]\n\n"
            f"Do not include the variation seed number in your response."
        )

def generate_item(item_type: str, rarity: str, material: str, style: str, genre: str) -> str:
    prompt = ItemPrompt().render(item_type=item_type, rarity=rarity, material=material, style=style, genre=genre)
    return call_openai(prompt)
