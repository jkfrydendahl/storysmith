from generators.openai import call_openai

class DeityPrompt:
    def __init__(self, domain: str = "", power_level: str = "", aspect: str = "", manifestation: str = "", genre: str = ""):
        self.domain = domain or "any domain"
        self.power_level = power_level or "any power level"
        self.aspect = aspect or "any aspect"
        self.manifestation = manifestation or "any manifestation"
        self.genre = genre or "fantasy"

    def render(self) -> str:
        return f"""Generate a detailed deity or divine entity for a tabletop RPG with the following parameters:
- Domain: {self.domain} (e.g., war, nature, death, knowledge, love, trickery, storms, forge, healing, chaos, etc.)
- Power Level: {self.power_level} (e.g., lesser deity, major deity, demigod, primordial, aspect, pantheon leader, etc.)
- Aspect: {self.aspect} (e.g., benevolent, wrathful, neutral, capricious, lawful, chaotic, compassionate, cruel, enigmatic, etc.)
- Manifestation: {self.manifestation} (e.g., visions, avatars, miracles, omens, silent, distant, active, embodied, etc.)
- Genre: {self.genre}

Create a comprehensive deity entry with the following sections:

## Divine Name and Titles
[Create a memorable name and 2-3 titles or epithets that reflect their nature]

## Description and Iconography
[Physical appearance when manifested, symbols, sacred colors, and how they're depicted in art - 2-3 sentences]

## Divine Domain and Portfolio
[What they govern, their sphere of influence, and associated concepts - 2 sentences]

## Personality and Aspect
[Their character, temperament, values, and how they relate to mortals - 2-3 sentences]

## Followers and Worshippers
[Who typically worships them, why people pray to them, and their faithful's characteristics - 2 sentences]

## Clergy and Practices
[How worship is organized, rituals, holy sites, and religious practices - 2-3 sentences]

## Divine Manifestation
[How they interact with the mortal world, signs of their presence, and intervention methods - 2 sentences]

## Myths and Legends
[Key stories, creation myths, or legendary deeds associated with this deity - 2-3 sentences]

## Relationships and Conflicts
[Allies among other deities, rivals, enemies, or divine relationships - 2 sentences]

## Sacred Items and Blessings
[Holy artifacts, divine boons granted to followers, or blessed items - 2 sentences]

## Adventure Hooks
[How the deity might involve characters in quests, divine missions, or conflicts - 2 sentences]

Keep the tone consistent with the {self.genre} genre. Make the deity memorable, thematically rich, and usable in campaigns. Consider how their power level affects their involvement in mortal affairs."""

def generate_deity(domain: str = "", power_level: str = "", aspect: str = "", manifestation: str = "", genre: str = "") -> str:
    prompt = DeityPrompt(domain, power_level, aspect, manifestation, genre)
    return call_openai(prompt.render())
