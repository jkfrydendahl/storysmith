import typer
from promts.npc import generate_npc

app = typer.Typer()

@app.command()
def npc(race: str = "human", gender: str = "female", char_class: str = "fighter", tone: str = "neutral", genre: str = "fantasy"):
    """Generate an NPC with specified traits."""
    result = generate_npc(race, gender, char_class, tone, genre)
    print("\n" + result)

if __name__ == "__main__":
    app()