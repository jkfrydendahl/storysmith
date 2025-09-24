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

# cd to storysmith root (repo) folder and run (in order):
poetry install
pip install "fastapi[standard]"
pip install openai
pip install typer
pip install react
pip install python-dotenv
```

Set your OpenAI API key:
```bash
# create .env file in the storysmith root folder (exluded in .gitignore to not reveal secrets)
# set your OPENAI_API_KEY in .env file
# file format: .env, contents: OPENAI_API_KEY=your-key-here
# to create your API key, go to https://platform.openai.com/api-keys
```

Run the CLI in terminal:
```bash
# cd to storysmith root folder
# run poetry call with the generator command you want to use

# example without parameters (for complete randomization):
poetry run python main.py character

# example, with parameters: 
poetry run python main.py character --race elf --gender female --char-class rogue --personality charlatan --genre fantasy
```

Run the web UI:
```bash
# from storysmith root folder, run:
poetry run uvicorn web.main:app --reload

# wait for the application startup to complete
# navigate to the /frontend folder and open index.html in your browser of choice

# note: to stop the web app, navigate to your terminal and press CTRL+C
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
- [x] Treasure
- [x] Adventures
- [ ] Events
- [ ] Organizations
- [ ] Regions
- [ ] Weather
