import os
import uvicorn
import time
from collections import defaultdict
from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from promts.character import generate_character
from promts.location import generate_location
from promts.item import generate_item
from promts.adventure import generate_adventure
from promts.treasure import generate_treasure
from promts.event import generate_event
from promts.organization import generate_organization
from promts.region import generate_region
from promts.weather import generate_weather

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Security: Restrict CORS to localhost only
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:5500",  # Common live server port
        "http://127.0.0.1:5500",
        "null",  # Allow file:// protocol for local development
    ],
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],
)

# Mount static files (frontend)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Simple rate limiter
rate_limit_storage = defaultdict(list)
RATE_LIMIT_REQUESTS = 10  # requests
RATE_LIMIT_WINDOW = 60    # seconds
RATE_LIMIT_CLEANUP_THRESHOLD = 1000  # Clean up when this many IPs are stored

def check_rate_limit(client_ip: str):
    """Simple rate limiter: 10 requests per 60 seconds per IP"""
    now = time.time()
    
    # Clean old entries for this IP
    rate_limit_storage[client_ip] = [
        timestamp for timestamp in rate_limit_storage[client_ip]
        if now - timestamp < RATE_LIMIT_WINDOW
    ]
    
    # Periodic cleanup of completely expired IPs to prevent memory leak
    if len(rate_limit_storage) > RATE_LIMIT_CLEANUP_THRESHOLD:
        expired_ips = [
            ip for ip, timestamps in rate_limit_storage.items()
            if not timestamps or (now - timestamps[-1]) > RATE_LIMIT_WINDOW
        ]
        for ip in expired_ips:
            del rate_limit_storage[ip]
    
    # Check limit
    if len(rate_limit_storage[client_ip]) >= RATE_LIMIT_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded. Max {RATE_LIMIT_REQUESTS} requests per {RATE_LIMIT_WINDOW} seconds."
        )
    
    # Add current request
    rate_limit_storage[client_ip].append(now)

def validate_input(value: str, max_length: int = 200, field_name: str = "Input") -> str:
    """Validate and sanitize user input"""
    if not value:
        return value
    
    # Strip whitespace
    value = value.strip()
    
    # Check length
    if len(value) > max_length:
        raise HTTPException(
            status_code=400,
            detail=f"{field_name} too long. Maximum {max_length} characters."
        )
    
    return value

@app.get('/', response_class=HTMLResponse)
async def root():
    """Serve the main frontend page"""
    file_path = os.path.join("frontend", "index.html")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return HTMLResponse(content=f.read())
    return PlainTextResponse(
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
        "- '/event' - Generate events\n"
        "- '/organization' - Generate organizations\n"
        "- '/region' - Generate regions\n"
        "- '/weather' - Generate weather\n"
        "\n"
        "Frontend available at: /static/index.html\n"
    )

@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join(app.root_path, file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})

@app.get("/npc")
def get_npc(
    request: Request,
    race: str = Query(""), 
    gender: str = Query(""), 
    char_class: str = Query(""), 
    personality: str = Query(""), 
    genre: str = Query("")
):
    # Rate limiting
    check_rate_limit(request.client.host)
    
    # Input validation
    race = validate_input(race, field_name="Race")
    gender = validate_input(gender, field_name="Gender")
    char_class = validate_input(char_class, field_name="Class")
    personality = validate_input(personality, field_name="Personality")
    genre = validate_input(genre, field_name="Genre")
    
    result = generate_character(race, gender, char_class, personality, genre)
    return {"npc": result}

@app.get("/location")
def get_location(
    request: Request,
    location_type: str = Query(""), 
    size: str = Query(""), 
    setting: str = Query(""), 
    tone: str = Query(""), 
    genre: str = Query("")
):
    # Rate limiting
    check_rate_limit(request.client.host)
    
    # Input validation
    location_type = validate_input(location_type, field_name="Location type")
    size = validate_input(size, field_name="Size")
    setting = validate_input(setting, field_name="Setting")
    tone = validate_input(tone, field_name="Tone")
    genre = validate_input(genre, field_name="Genre")
    
    result = generate_location(location_type, size, setting, tone, genre)
    return {"location": result}

@app.get("/item")
def get_item(
    request: Request,
    item_type: str = Query(""), 
    rarity: str = Query(""), 
    material: str = Query(""), 
    style: str = Query(""), 
    genre: str = Query("")
):
    check_rate_limit(request.client.host)
    item_type = validate_input(item_type, field_name="Item type")
    rarity = validate_input(rarity, field_name="Rarity")
    material = validate_input(material, field_name="Material")
    style = validate_input(style, field_name="Style")
    genre = validate_input(genre, field_name="Genre")
    result = generate_item(item_type, rarity, material, style, genre)
    return {"item": result}

@app.get("/adventure")
def get_adventure(
    request: Request,
    adventure_type: str = Query(""), 
    length: str = Query(""), 
    theme: str = Query(""), 
    difficulty: str = Query(""), 
    genre: str = Query("")
):
    check_rate_limit(request.client.host)
    adventure_type = validate_input(adventure_type, field_name="Adventure type")
    length = validate_input(length, field_name="Length")
    theme = validate_input(theme, field_name="Theme")
    difficulty = validate_input(difficulty, field_name="Difficulty")
    genre = validate_input(genre, field_name="Genre")
    result = generate_adventure(adventure_type, length, theme, difficulty, genre)
    return {"adventure": result}

@app.get("/treasure")
def get_treasure(
    request: Request,
    treasure_type: str = Query(""), 
    value: str = Query(""), 
    origin: str = Query(""), 
    condition: str = Query(""), 
    genre: str = Query("")
):
    check_rate_limit(request.client.host)
    treasure_type = validate_input(treasure_type, field_name="Treasure type")
    value = validate_input(value, field_name="Value")
    origin = validate_input(origin, field_name="Origin")
    condition = validate_input(condition, field_name="Condition")
    genre = validate_input(genre, field_name="Genre")
    result = generate_treasure(treasure_type, value, origin, condition, genre)
    return {"treasure": result}

@app.get("/event")
def get_event(
    request: Request,
    event_type: str = Query(""), 
    scale: str = Query(""), 
    tone: str = Query(""), 
    setting: str = Query(""), 
    genre: str = Query("")
):
    check_rate_limit(request.client.host)
    event_type = validate_input(event_type, field_name="Event type")
    scale = validate_input(scale, field_name="Scale")
    tone = validate_input(tone, field_name="Tone")
    setting = validate_input(setting, field_name="Setting")
    genre = validate_input(genre, field_name="Genre")
    result = generate_event(event_type, scale, tone, setting, genre)
    return {"event": result}

@app.get("/organization")
def get_organization(
    request: Request,
    org_type: str = Query(""), 
    size: str = Query(""), 
    influence: str = Query(""), 
    focus: str = Query(""), 
    genre: str = Query("")
):
    check_rate_limit(request.client.host)
    org_type = validate_input(org_type, field_name="Organization type")
    size = validate_input(size, field_name="Size")
    influence = validate_input(influence, field_name="Influence")
    focus = validate_input(focus, field_name="Focus")
    genre = validate_input(genre, field_name="Genre")
    result = generate_organization(org_type, size, influence, focus, genre)
    return {"organization": result}

@app.get("/region")
def get_region(
    request: Request,
    region_type: str = Query(""), 
    size: str = Query(""), 
    terrain: str = Query(""), 
    climate: str = Query(""), 
    genre: str = Query("")
):
    check_rate_limit(request.client.host)
    region_type = validate_input(region_type, field_name="Region type")
    size = validate_input(size, field_name="Size")
    terrain = validate_input(terrain, field_name="Terrain")
    climate = validate_input(climate, field_name="Climate")
    genre = validate_input(genre, field_name="Genre")
    result = generate_region(region_type, size, terrain, climate, genre)
    return {"region": result}

@app.get("/weather")
def get_weather(
    request: Request,
    weather_type: str = Query(""), 
    severity: str = Query(""), 
    season: str = Query(""), 
    environment: str = Query(""), 
    genre: str = Query("")
):
    check_rate_limit(request.client.host)
    weather_type = validate_input(weather_type, field_name="Weather type")
    severity = validate_input(severity, field_name="Severity")
    season = validate_input(season, field_name="Season")
    environment = validate_input(environment, field_name="Environment")
    genre = validate_input(genre, field_name="Genre")
    result = generate_weather(weather_type, severity, season, environment, genre)
    return {"weather": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)