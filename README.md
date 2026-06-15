# Odoo CustomApp
[AI Projects 2] This project is part of a series of small AI projects

An Odoo custom module that integrates the Meeting Summarizer AI ([AI Projects 1]) service directly into Odoo.


## Project Structure

```text
.
├── controllers/
│   └── ...
├── demo/
│   └── ...
├── models/
│   └── ...
├── security/
│   └── ...
├── views/
│   └── ...
├── .gitignore
├── README.md
├── __init__.py
└── __manifest__.py
```

## Requirements

- Python 3.10+
- Ollama installed locally

### Ollama Models

Pull the required models or change the model in backend .env file:

```bash
ollama pull llama3.1:8b
```
