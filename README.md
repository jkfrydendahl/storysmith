# 🎩 Storysmith

**Storysmith** is a modular, AI-powered storytelling toolkit for tabletop RPG creators. Generate rich characters, locations, items, and more — through a simple CLI or API.

---

## ✨ Features

- 🔮 Prompt-based generation for RPG elements
- 💻 CLI-first, with pluggable model backends
- 🧱 Clean code and extensible architecture
- ⚖️ DevEx-friendly: built with testing, linting, CI

---

---

## 🛠️ Installation and Usage

```bash
git clone https://github.com/your-username/storysmith.git
cd storysmith
poetry install
pip install "fastapi[standard]"
pip install openai
pip install typer
pip install
```

Set your OpenAI API key:
```bash
in file generators/openai.py
```

Run the CLI:
```bash
poetry env activate
poetry run python main.py

example with parameters: poetry run python main.py --race elf --char-class rogue --tone dark --genre fantasy  
```

Run the Web UI:
```bash
poetry run uvicorn web.main:app --reload
```

To use the frontend:
```bash
cd frontend
npm install
npm run dev
```

---

## 🔍 Roadmap

- [x] Web UI (FastAPI API backend)
- [x] Frontend UI (React + Vite)
- [ ] Local model support (e.g., Ollama)
- [ ] Prompt customization via YAML/JSON
- [ ] Campaign export to Obsidian/Markdown
