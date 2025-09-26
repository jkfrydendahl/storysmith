import typer
from promts.character import generate_character
from promts.location import generate_location
from promts.item import generate_item
from promts.adventure import generate_adventure
from promts.treasure import generate_treasure
from promts.event import generate_event
from promts.organization import generate_organization

app = typer.Typer()

@app.command()
def character(race: str = "", gender: str = "", char_class: str = "", personality: str = "", genre: str = ""):
    """Generate a character with specified traits. Leave parameters empty for complete randomization."""
    result = generate_character(race, gender, char_class, personality, genre)
    print("\n" + result)

@app.command()
def location(location_type: str = "", size: str = "", setting: str = "", tone: str = "", genre: str = ""):
    """Generate a location with specified traits. Leave parameters empty for complete randomization. Tone refers to atmosphere/condition (e.g., posh, dirty, welcoming, abandoned)."""
    result = generate_location(location_type, size, setting, tone, genre)
    print("\n" + result)

@app.command()
def item(item_type: str = "", rarity: str = "", material: str = "", style: str = "", genre: str = ""):
    """Generate an item with specified traits. Leave parameters empty for complete randomization. Style refers to appearance/design (e.g., ornate, crude, mysterious, elegant)."""
    result = generate_item(item_type, rarity, material, style, genre)
    print("\n" + result)

@app.command()
def adventure(adventure_type: str = "", length: str = "", theme: str = "", difficulty: str = "", genre: str = ""):
    """Generate an adventure with specified traits. Leave parameters empty for complete randomization. Adventure type could be dungeon, investigation, rescue, heist, etc."""
    result = generate_adventure(adventure_type, length, theme, difficulty, genre)
    print("\n" + result)

@app.command()
def treasure(treasure_type: str = "", value: str = "", origin: str = "", condition: str = "", genre: str = ""):
    """Generate treasures and trinkets with specified traits. Leave parameters empty for complete randomization. Type could be hoard, jewelry, coins, artifact, etc."""
    result = generate_treasure(treasure_type, value, origin, condition, genre)
    print("\n" + result)

@app.command()
def event(event_type: str = "", scale: str = "", tone: str = "", setting: str = "", genre: str = ""):
    """Generate an event with specified traits. Leave parameters empty for complete randomization. Events are atmospheric happenings that occur in the world."""
    result = generate_event(event_type, scale, tone, setting, genre)
    print("\n" + result)

@app.command()
def organization(org_type: str = "", size: str = "", influence: str = "", focus: str = "", genre: str = ""):
    """Generate an organization with specified traits. Leave parameters empty for complete randomization. Organizations include guilds, cults, companies, noble houses, etc."""
    result = generate_organization(org_type, size, influence, focus, genre)
    print("\n" + result)

if __name__ == "__main__":
    app()