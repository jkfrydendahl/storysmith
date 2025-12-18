from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class OrganizationPrompt(PromptTemplate):
    def render(self, structure: str, size: str, influence: str, focus: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        
        # Handle empty parameters by using descriptive language
        structure_param = structure if structure.strip() and structure.strip().lower() != "undefined" else "interesting organization"
        size_param = size if size.strip() and size.strip().lower() != "undefined" else "appropriate size"
        influence_param = influence if influence.strip() and influence.strip().lower() != "undefined" else "suitable influence"
        focus_param = focus if focus.strip() and focus.strip().lower() != "undefined" else "meaningful purpose"
        genre_param = genre if genre.strip() and genre.strip().lower() != "undefined" else "fantasy setting"
        
        return (
            f"Create a unique tabletop RPG organization with the following parameters:\n"
            f"Structure: {structure_param}\n"
            f"Size: {size_param}\n"
            f"Influence: {influence_param}\n"
            f"Focus: {focus_param}\n"
            f"Genre: {genre_param}\n"
            f"Variation seed: {random_seed}\n\n"
            f"IMPORTANT: Ensure the organization's scope and influence match the specified size and influence level:\n"
            f"- Small + Local: 5-20 members, single location, neighborhood influence\n"
            f"- Medium + Regional: 50-200 members, multiple locations, city/province influence\n"
            f"- Large + National: 500+ members, many chapters, country-wide influence\n"
            f"- Massive + International: Thousands of members, global reach, multi-nation influence\n\n"
            f"Format your response with clear headings:\n\n"
            f"Organization Name: [Give it a memorable, evocative name]\n\n"
            f"Mission and Purpose: [Their goals, beliefs, and reason for existence]\n\n"
            f"Structure and Hierarchy: [Leadership, ranks, and how they organize - appropriate to size]\n\n"
            f"Key Members: [Important leaders and notable figures - number should match size]\n\n"
            f"Operations and Activities: [What they do, how they operate, methods and practices]\n\n"
            f"Resources and Assets: [Wealth, properties, connections, and capabilities - match influence level]\n\n"
            f"Secrets and Mysteries: [Hidden agendas, internal conflicts, or unknown aspects]\n\n"
            f"Adventure Hooks: [How the party might interact with, oppose, or work for this organization]\n\n"
            f"Do not include the variation seed number in your response."
        )

def generate_organization(structure: str, size: str, influence: str, focus: str, genre: str) -> str:
    prompt = OrganizationPrompt().render(structure=structure, size=size, influence=influence, focus=focus, genre=genre)
    return call_openai(prompt)
