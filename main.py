import typer
from promts.character import generate_character
from promts.location import generate_location
from promts.item import generate_item
from promts.adventure import generate_adventure

app = typer.Typer()

@app.command()
def character(race: str = "human", gender: str = "female", char_class: str = "fighter", personality: str = "neutral", genre: str = "fantasy"):
    """Generate a character with specified traits."""
    result = generate_character(race, gender, char_class, personality, genre)
    print("\n" + result)

@app.command()
def location(location_type: str = "tavern", size: str = "medium", setting: str = "city", tone: str = "welcoming", genre: str = "fantasy"):
    """Generate a location with specified traits. Tone refers to atmosphere/condition (e.g., posh, dirty, welcoming, abandoned)."""
    result = generate_location(location_type, size, setting, tone, genre)
    print("\n" + result)

@app.command()
def item(item_type: str = "weapon", rarity: str = "common", material: str = "steel", style: str = "practical", genre: str = "fantasy"):
    """Generate an item with specified traits. Style refers to appearance/design (e.g., ornate, crude, mysterious, elegant)."""
    result = generate_item(item_type, rarity, material, style, genre)
    print("\n" + result)

@app.command()
def adventure(adventure_type: str = "dungeon", length: str = "short", theme: str = "exploration", difficulty: str = "medium", genre: str = "fantasy"):
    """Generate an adventure with specified traits. Adventure type could be dungeon, investigation, rescue, heist, etc."""
    result = generate_adventure(adventure_type, length, theme, difficulty, genre)
    print("\n" + result)

if __name__ == "__main__":
    app()