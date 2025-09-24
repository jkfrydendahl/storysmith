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

# cd to storysmith repo folder and run:
poetry install
pip install "fastapi[standard]"
pip install openai
pip install typer
pip install react
pip install python-dotenv
```

Set your OpenAI API key:
```bash
# set your OPENAI_API_KEY in .env file
# (exluded in .gitignore to not reveal secrets)
```

Run the CLI in terminal:
```bash
# go to storysmith root folder and run:
poetry run python main.py

# example with parameters: 
poetry run python main.py --race elf --gender male --char-class rogue --tone dark --genre fantasy  
```

Run the web UI:
```bash
# go to storysmith root folder and run:
poetry run uvicorn web.main:app --reload

# wait for the application startup to complete
# navigate to the /frontend folder and open index.html in your browser of choice
```

---

## 🔍 Roadmap

Solution:
- [x] Web UI 
- [x] Frontend UI
- [ ] Local model support
- [ ] Advanced prompt customization
- [ ] Bulk generation
- [ ] History/search functionality
- [ ] Randomization controls

Features
- [x] Characters
- [x] Locations
- [x] Items
- [ ] Adventures
- [ ] Events
- [ ] Organizations
- [ ] Treasure
- [ ] Regions
- [ ] Weather
