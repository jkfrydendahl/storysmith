import typer
from promts.npc import generate_npc
from promts.location import generate_location

app = typer.Typer()

@app.command()
def npc(race: str = "human", gender: str = "female", char_class: str = "fighter", tone: str = "neutral", genre: str = "fantasy"):
    """Generate an NPC with specified traits."""
    result = generate_npc(race, gender, char_class, tone, genre)
    print("\n" + result)

@app.command()
def location(location_type: str = "tavern", size: str = "medium", setting: str = "city", tone: str = "welcoming", genre: str = "fantasy"):
    """Generate a location with specified traits. Tone refers to atmosphere/condition (e.g., posh, dirty, welcoming, abandoned)."""
    result = generate_location(location_type, size, setting, tone, genre)
    print("\n" + result)

if __name__ == "__main__":
    app()