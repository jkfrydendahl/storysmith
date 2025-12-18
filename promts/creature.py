from generators.openai import call_openai

class CreaturePrompt:
    def __init__(self, species: str = "", size: str = "", behavior: str = "", habitat: str = "", genre: str = ""):
        self.species = species or "any species"
        self.size = size or "any size"
        self.behavior = behavior or "any behavior"
        self.habitat = habitat or "any habitat"
        self.genre = genre or "fantasy"

    def render(self) -> str:
        return f"""Generate a detailed creature for a tabletop RPG with the following parameters:
- Species: {self.species} (e.g., beast, dragon, undead, aberration, elemental, fey, fiend, construct, humanoid, etc.)
- Size: {self.size} (e.g., tiny, small, medium, large, huge, gargantuan)
- Behavior: {self.behavior} (e.g., aggressive, passive, territorial, curious, cunning, mindless, protective, predatory, etc.)
- Habitat: {self.habitat} (e.g., forest, desert, mountains, underground, aquatic, urban, etc.)
- Genre: {self.genre}

Create a comprehensive creature entry with the following sections:

## Creature Name
[Create a memorable and evocative name]

## Description
[Physical appearance, notable features, size comparison, and sensory details - 2-3 sentences]

## Behavior and Tactics
[How the creature acts in combat and social situations, hunting patterns, intelligence level - 2-3 sentences]

## Habitat and Ecology
[Where it lives, what it eats, how it fits into the ecosystem - 2 sentences]

## Abilities and Powers
[Special abilities, magical powers, unique attacks - list 2-4 abilities with brief descriptions]

## Weaknesses and Vulnerabilities
[What the creature is vulnerable to, how to defeat it - 1-2 sentences]

## Treasure and Loot
[What valuable items or materials the creature might have or drop - 1-2 sentences]

## Lore and Origin
[Legends, myths, or backstory about the creature - 2-3 sentences]

## Encounter Suggestions
[How to use this creature in a game, challenge rating considerations, group tactics - 2 sentences]

Keep the tone consistent with the {self.genre} genre. Make the creature memorable, balanced, and usable in gameplay. Focus on vivid descriptions and practical game mechanics."""

def generate_creature(species: str = "", size: str = "", behavior: str = "", habitat: str = "", genre: str = "") -> str:
    prompt = CreaturePrompt(species, size, behavior, habitat, genre)
    return call_openai(prompt.render())
