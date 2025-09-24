# 🎩 Storysmith

**Storysmith** is a modular, AI-powered storytelling toolkit for tabletop RPG creators. Generate rich characters, locations, items, and more — through a simple CLI or API. See roadmap at the bottom for status on feature implementation.

---

## ✨ Features

- 🔮 Prompt-based generation for RPG elements
- 💻 CLI-first, with pluggable model backends
- 🧱 Clean code and extensible architecture

---

## 🛠️ Installation and Usage

Prerequisites: 
- Python 3.11 or newer. Download from https://www.python.org/downloads/
- OpenAI API Key. More info: https://platform.openai.com/docs/overview

Installation:
```bash
git clone https://github.com/JesperKF311/storysmith.git
cd storysmith
poetry install
pip install "fastapi[standard]"
pip install openai
pip install typer
pip install react
pip install python-dotenv
```

Set your OpenAI API key:
```bash
set OPENAI_API_KEY in .env file
(exluded in .gitignore to not reveal secrets)
```

Run the CLI in terminal:
```bash
poetry run python main.py

// Example with parameters: 
poetry run python main.py --race elf --gender male --char-class rogue --tone dark --genre fantasy  
```

Run the web UI:
```bash
poetry run uvicorn web.main:app --reload

wait for the application startup to complete
navigate to the /frontend folder and open index.html in your browser of choice
```

---

## 🔍 Roadmap

Solution:
- [x] Web UI (FastAPI API backend)
- [x] Frontend UI (HTML and JS)
- [ ] Local model support (e.g., Ollama)
- [ ] Prompt customization via YAML/JSON
- [ ] Campaign export to Obsidian/Markdown

Features
- [x] Characters
- [x] Locations
- [ ] Items
- [ ] Regions
- [ ] Adventures
- [ ] Events
- [ ] Organizations
- [ ] Treasure
- [ ] Weather
