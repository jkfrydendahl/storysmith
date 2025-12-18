from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class TreasurePrompt(PromptTemplate):
    def render(self, category: str, value: str, origin: str, condition: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        
        # Handle empty parameters by using "random" or more descriptive language
        category_param = category if category.strip() and category.strip().lower() != "undefined" else "random treasure or trinket"
        value_param = value if value.strip() and value.strip().lower() != "undefined" else "appropriate value"
        origin_param = origin if origin.strip() and origin.strip().lower() != "undefined" else "mysterious origin"
        condition_param = condition if condition.strip() and condition.strip().lower() != "undefined" else "varying condition"
        genre_param = genre if genre.strip() and genre.strip().lower() != "undefined" else "fantasy setting"
        
        return (
            f"Create a unique tabletop RPG treasure or trinket with the following parameters:\n"
            f"Category: {category_param}\n"
            f"Value: {value_param}\n"
            f"Origin: {origin_param}\n"
            f"Condition: {condition_param}\n"
            f"Genre: {genre_param}\n"
            f"Variation seed: {random_seed}\n\n"
            f"IMPORTANT: Pay close attention to the specified value level. If a specific value is given (like 'legendary', 'worthless', 'precious', etc.), ensure the treasure's description, rarity, and monetary worth clearly reflect that value tier.\n\n"
            f"Format your response with clear headings:\n\n"
            f"Name: [Give it an evocative, memorable name]\n\n"
            f"Description: [Vivid description of appearance, materials, and craftsmanship]\n\n"
            f"Contents (if applicable): [What's inside, individual items, or components]\n\n"
            f"Value and Rarity: [Monetary worth, trade value, or significance - must match the specified value parameter]\n\n"
            f"History and Provenance: [Origin story, previous owners, or legendary status]\n\n"
            f"Special Properties: [Magical effects, curses, hidden features, or unique qualities]\n\n"
            f"Adventure Hooks: [Plot possibilities, complications, or reasons someone might seek this treasure]\n\n"
            f"Do not include the variation seed number in your response."
        )

def generate_treasure(category: str, value: str, origin: str, condition: str, genre: str) -> str:
    prompt = TreasurePrompt().render(category=category, value=value, origin=origin, condition=condition, genre=genre)
    return call_openai(prompt)
