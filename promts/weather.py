from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class WeatherPrompt(PromptTemplate):
    def render(self, phenomenon: str, severity: str, season: str, environment: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        
        # Handle empty parameters by using descriptive language
        phenomenon_param = phenomenon if phenomenon.strip() and phenomenon.strip().lower() != "undefined" else "interesting weather"
        severity_param = severity if severity.strip() and severity.strip().lower() != "undefined" else "appropriate severity"
        season_param = season if season.strip() and season.strip().lower() != "undefined" else "any season"
        environment_param = environment if environment.strip() and environment.strip().lower() != "undefined" else "suitable environment"
        genre_param = genre if genre.strip() and genre.strip().lower() != "undefined" else "fantasy setting"
        
        return (
            f"Create a unique tabletop RPG weather event with the following parameters:\n"
            f"Phenomenon: {phenomenon_param}\n"
            f"Severity: {severity_param}\n"
            f"Season: {season_param}\n"
            f"Environment: {environment_param}\n"
            f"Genre: {genre_param}\n"
            f"Variation seed: {random_seed}\n\n"
            f"IMPORTANT: Ensure the weather's severity matches the specified level:\n"
            f"- Mild: Noticeable but not hindering (light rain, gentle breeze, mild heat)\n"
            f"- Moderate: Affects travel and comfort (steady rain, strong winds, hot/cold)\n"
            f"- Severe: Dangerous and hindering (heavy storm, blizzard, extreme temperatures)\n"
            f"- Catastrophic: Life-threatening and devastating (hurricane, tornado, supernatural storm)\n\n"
            f"Format your response with clear headings:\n\n"
            f"Current Conditions: [What the weather is like right now - temperature, precipitation, wind, visibility]\n\n"
            f"Atmospheric Effects: [Sensory details - what characters see, hear, feel, smell]\n\n"
            f"Mechanical Effects: [Game impacts - travel speed, visibility penalties, skill check modifiers, damage]\n\n"
            f"Duration and Progression: [How long it lasts, how it develops or changes]\n\n"
            f"Dangers and Hazards: [Specific threats - exposure, flooding, lightning, environmental damage]\n\n"
            f"Sheltering and Survival: [How to protect against it, what resources help, safe locations]\n\n"
            f"Aftermath: [What remains after the weather passes - damage, changes to terrain, lingering effects]\n\n"
            f"Do not include the variation seed number in your response."
        )

def generate_weather(phenomenon: str, severity: str, season: str, environment: str, genre: str) -> str:
    prompt = WeatherPrompt().render(phenomenon=phenomenon, severity=severity, season=season, environment=environment, genre=genre)
    return call_openai(prompt)
