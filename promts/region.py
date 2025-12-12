from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class RegionPrompt(PromptTemplate):
    def render(self, region_type: str, size: str, terrain: str, climate: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        
        # Handle empty parameters by using descriptive language
        type_param = region_type if region_type.strip() and region_type.strip().lower() != "undefined" else "interesting region"
        size_param = size if size.strip() and size.strip().lower() != "undefined" else "appropriate size"
        terrain_param = terrain if terrain.strip() and terrain.strip().lower() != "undefined" else "varied terrain"
        climate_param = climate if climate.strip() and climate.strip().lower() != "undefined" else "suitable climate"
        genre_param = genre if genre.strip() and genre.strip().lower() != "undefined" else "fantasy setting"
        
        return (
            f"Create a unique tabletop RPG region with the following parameters:\n"
            f"Region Type: {type_param}\n"
            f"Size: {size_param}\n"
            f"Terrain: {terrain_param}\n"
            f"Climate: {climate_param}\n"
            f"Genre: {genre_param}\n"
            f"Variation seed: {random_seed}\n\n"
            f"IMPORTANT: Ensure the region's scope matches the specified size:\n"
            f"- Small: A county, valley, or city-state (days to cross)\n"
            f"- Medium: A province, duchy, or small kingdom (weeks to cross)\n"
            f"- Large: A kingdom, large nation, or major territory (months to cross)\n"
            f"- Vast: An empire, continent, or massive domain (seasons to cross)\n\n"
            f"Format your response with clear headings:\n\n"
            f"Region Name: [Give it an evocative, memorable name]\n\n"
            f"Geography and Landscape: [Describe the terrain, major features, and natural landmarks - match terrain and size]\n\n"
            f"Climate and Seasons: [Weather patterns, seasonal changes, environmental conditions - match climate]\n\n"
            f"Population and Settlements: [Major cities, towns, villages, and demographics - appropriate to size]\n\n"
            f"Culture and Society: [Customs, traditions, social structure, and way of life]\n\n"
            f"Government and Politics: [Leadership, power structures, laws, and conflicts - scale to size]\n\n"
            f"Economy and Resources: [Trade goods, natural resources, economic activities]\n\n"
            f"Notable Locations: [Key places of interest, landmarks, or significant sites within the region]\n\n"
            f"Threats and Conflicts: [Dangers, tensions, enemies, or ongoing struggles]\n\n"
            f"Adventure Hooks: [Reasons adventurers might visit or get involved with this region]\n\n"
            f"Do not include the variation seed number in your response."
        )

def generate_region(region_type: str, size: str, terrain: str, climate: str, genre: str) -> str:
    prompt = RegionPrompt().render(region_type=region_type, size=size, terrain=terrain, climate=climate, genre=genre)
    return call_openai(prompt)