# 🎩 Storysmith

**Storysmith** is a modular, AI-powered storytelling toolkit for tabletop RPG creators. Generate rich characters, locations, items, and more — through a simple CLI or API.

---

## ✨ Features

- 🔮 Prompt-based generation for RPG elements
- 💻 CLI-first, with pluggable model backends
- 🧱 Clean code and extensible architecture
- ⚖️ DevEx-friendly: built with testing, linting, CI

---

## 🚀 Usage

### CLI
```bash
storysmith npc --race elf --char-class rogue --tone dark
```

### Web API
```bash
GET /npc?race=elf&char_class=rogue&tone=dark
```

Run locally:
```bash
poetry run uvicorn web.main:app --reload
```

---

## 🛠️ Install

```bash
git clone https://github.com/your-username/storysmith.git
cd storysmith
poetry install
```

Set your OpenAI API key:
```bash
export OPENAI_API_KEY=your-key
```

Run the CLI:
```bash
poetry run python cli.py npc --race elf --char-class rogue --tone dark
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
