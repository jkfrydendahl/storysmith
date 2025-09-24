import os
import uvicorn
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from promts.character import generate_character
from promts.location import generate_location
from promts.item import generate_item
from promts.adventure import generate_adventure
from promts.treasure import generate_treasure

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', response_class=PlainTextResponse)
def default():
    return (
        "Welcome to *Storysmith*\n" 
        "- a modular, AI-powered storytelling toolkit for tabletop RPG creators.\n"
        "Generate rich characters, locations, items, and more — through a simple CLI or API.\n"
        "\n"
        "Available endpoints:\n"
        "- '/npc' - Generate characters\n"
        "- '/location' - Generate locations\n"
        "- '/item' - Generate items\n"
        "- '/adventure' - Generate adventures\n"
        "- '/treasure' - Generate treasures and trinkets\n"
        "\n"
        "More features coming soon!\n"
    )

@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join(app.root_path, file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})

@app.get("/npc")
def get_npc(race: str = Query("human"), gender = Query("female"), char_class: str = Query("fighter"), personality: str = Query("neutral"), genre: str = Query("fantasy")):
    result = generate_character(race, gender, char_class, personality, genre)
    return {"npc": result}

@app.get("/location")
def get_location(location_type: str = Query("tavern"), size: str = Query("medium"), setting: str = Query("city"), tone: str = Query("welcoming"), genre: str = Query("fantasy")):
    result = generate_location(location_type, size, setting, tone, genre)
    return {"location": result}

@app.get("/item")
def get_item(item_type: str = Query("weapon"), rarity: str = Query("common"), material: str = Query("steel"), style: str = Query("practical"), genre: str = Query("fantasy")):
    result = generate_item(item_type, rarity, material, style, genre)
    return {"item": result}

@app.get("/adventure")
def get_adventure(adventure_type: str = Query("dungeon"), length: str = Query("short"), theme: str = Query("exploration"), difficulty: str = Query("medium"), genre: str = Query("fantasy")):
    result = generate_adventure(adventure_type, length, theme, difficulty, genre)
    return {"adventure": result}

@app.get("/treasure")
def get_treasure(treasure_type: str = Query(""), value: str = Query(""), origin: str = Query(""), condition: str = Query(""), genre: str = Query("")):
    result = generate_treasure(treasure_type, value, origin, condition, genre)
    return {"treasure": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)