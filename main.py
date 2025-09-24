import typer
from promts.character import generate_character
from promts.location import generate_location
from promts.item import generate_item

app = typer.Typer()

@app.command()
def character(race: str = "human", gender: str = "female", char_class: str = "fighter", tone: str = "neutral", genre: str = "fantasy"):
    """Generate a character with specified traits."""
    result = generate_character(race, gender, char_class, tone, genre)
    print("\n" + result)

@app.command()
def location(location_type: str = "tavern", size: str = "medium", setting: str = "city", tone: str = "welcoming", genre: str = "fantasy"):
    """Generate a location with specified traits. Tone refers to atmosphere/condition (e.g., posh, dirty, welcoming, abandoned)."""
    result = generate_location(location_type, size, setting, tone, genre)
    print("\n" + result)

@app.command()
def item(item_type: str = "weapon", rarity: str = "common", material: str = "steel", tone: str = "practical", genre: str = "fantasy"):
    """Generate an item with specified traits. Tone refers to style/appearance (e.g., ornate, crude, mysterious, elegant)."""
    result = generate_item(item_type, rarity, material, tone, genre)
    print("\n" + result)

if __name__ == "__main__":
    app()