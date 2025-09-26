from promts.base import PromptTemplate
from generators.openai import call_openai
import random

class EventPrompt(PromptTemplate):
    def render(self, event_type: str, scale: str, tone: str, setting: str, genre: str) -> str:
        random_seed = random.randint(1000, 9999)
        
        # Handle empty parameters by using descriptive language
        type_param = event_type if event_type.strip() and event_type.strip().lower() != "undefined" else "interesting event"
        scale_param = scale if scale.strip() and scale.strip().lower() != "undefined" else "appropriate scale"
        tone_param = tone if tone.strip() and tone.strip().lower() != "undefined" else "suitable atmosphere"
        setting_param = setting if setting.strip() and setting.strip().lower() != "undefined" else "fitting location"
        genre_param = genre if genre.strip() and genre.strip().lower() != "undefined" else "fantasy setting"
        
        return (
            f"Create a unique tabletop RPG event with the following parameters:\n"
            f"Event Type: {type_param}\n"
            f"Scale: {scale_param}\n"
            f"Tone: {tone_param}\n"
            f"Setting: {setting_param}\n"
            f"Genre: {genre_param}\n"
            f"Variation seed: {random_seed}\n\n"
            f"IMPORTANT: Pay close attention to the SCALE parameter. The event must match the specified scale:\n"
            f"- Personal: Affects only 1-3 individuals directly (a conversation, personal accident, individual discovery)\n"
            f"- Local: Affects a small area like a neighborhood, single building, or small group (shop incident, street commotion)\n"
            f"- Regional: Affects a town, city district, or rural area (festival, natural disaster affecting one settlement)\n"
            f"- Kingdom-wide: Affects an entire nation or large region (war declaration, major political change)\n"
            f"- Cosmic: Affects multiple worlds or planes of existence (divine intervention, planar shifts)\n\n"
            f"Format your response with clear headings:\n\n"
            f"Event Name: [Give it a memorable, descriptive name appropriate to the scale]\n\n"
            f"What's Happening: [Clear description of the event as it unfolds - must match the specified scale]\n\n"
            f"Atmosphere and Details: [Sensory details, mood, what people see/hear/feel]\n\n"
            f"Key Participants: [Who's involved, their reactions and motivations - number should match scale]\n\n"
            f"Immediate Consequences: [Direct effects and reactions in the moment - scope must match scale]\n\n"
            f"Potential Developments: [How this might evolve or what it could lead to]\n\n"
            f"Party Integration: [How the party might encounter, witness, or be affected by this event]\n\n"
            f"Do not include the variation seed number in your response."
        )

def generate_event(event_type: str, scale: str, tone: str, setting: str, genre: str) -> str:
    prompt = EventPrompt().render(event_type=event_type, scale=scale, tone=tone, setting=setting, genre=genre)
    return call_openai(prompt)
