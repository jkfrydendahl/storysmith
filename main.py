import typer
from storysmith.prompts.npc import generate_npc

app = typer.Typer()

@app.command()
def npc(race: str = "human", char_class: str = "fighter", tone: str = "neutral"):
    """Generate an NPC with specified traits."""
    result = generate_npc(race, char_class, tone)
    print("\n" + result)

if __name__ == "__main__":
    app()