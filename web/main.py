from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from storysmith.prompts.npc import generate_npc

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/npc")
def get_npc(race: str = Query("human"), char_class: str = Query("fighter"), tone: str = Query("neutral")):
    result = generate_npc(race, char_class, tone)
    return {"npc": result}