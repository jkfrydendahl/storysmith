from generators.openai import call_openai

class SpellPrompt:
    def __init__(self, effect: str = "", power_level: str = "", school: str = "", casting_method: str = "", genre: str = ""):
        self.effect = effect or "any effect"
        self.power_level = power_level or "any power level"
        self.school = school or "any school"
        self.casting_method = casting_method or "any casting method"
        self.genre = genre or "fantasy"

    def render(self) -> str:
        return f"""Generate a detailed spell or magical ability for a tabletop RPG with the following parameters:
- Effect: {self.effect} (e.g., damage, protection, control, enhancement, debuff, healing, summoning, transformation, etc.)
- Power Level: {self.power_level} (e.g., cantrip/minor, low, moderate, high, ultimate/legendary)
- School: {self.school} (e.g., fire, ice, lightning, nature, shadow, light, arcane, necromancy, illusion, etc.)
- Casting Method: {self.casting_method} (e.g., instant, ritual, channeled, concentration, triggered, prepared, improvised, etc.)
- Genre: {self.genre}

Create a comprehensive spell entry with the following sections:

## Spell Name
[Create an evocative and memorable name that reflects the spell's nature]

## Description
[Visual and sensory description of what happens when the spell is cast - 2-3 sentences]

## Casting Requirements
[What's needed to cast: components, gestures, verbal requirements, preparation time - 2 sentences]

## Magical Effect
[Detailed explanation of what the spell does mechanically and narratively - 2-3 sentences]

## Range and Duration
[How far it reaches, how long it lasts, and any area of effect - 1-2 sentences]

## Limitations and Drawbacks
[Costs, restrictions, weaknesses, or side effects - 2 sentences]

## Synergies and Combinations
[How it works with other magic, what enhances or counters it - 1-2 sentences]

## Lore and Origin
[History, who created it, cultural significance, or mystical backstory - 2-3 sentences]

## Usage Examples
[Tactical suggestions, creative applications, and gameplay scenarios - 2 sentences]

Keep the tone consistent with the {self.genre} genre. Make the spell balanced, flavorful, and interesting to use. Focus on both mechanical clarity and narrative impact. Consider how the casting method affects the spell's use in gameplay."""

def generate_spell(effect: str = "", power_level: str = "", school: str = "", casting_method: str = "", genre: str = "") -> str:
    prompt = SpellPrompt(effect, power_level, school, casting_method, genre)
    return call_openai(prompt.render())
