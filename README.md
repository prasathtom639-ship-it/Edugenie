# EduGenie-AI

EduGenie-AI is an AI-powered educational assistant designed to support students with learning activities such as question answering, concept explanations, quizzes, summaries, and personalized learning paths.

## Features

- AI-based Question Answering
- Concept Explanation
- Quiz Generation
- Learning Path Generation
- Study Summary
- Student-focused learning assistance

## Project Structure

```text
EduGenie-AI/
├── static/
├── templates/
├── ai_client.py
├── config.py
├── explanation_module.py
├── learning_path.py
├── main.py
├── models.py
├── prompts.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── requirements
├── requirements-local
├── .env.example
├── .gitignore
└── README.md
```

## Main Modules

- `main.py` – Main application entry point.
- `ai_client.py` – AI service/client integration.
- `config.py` – Application configuration.
- `qna.py` – Question-answering functionality.
- `explanation_module.py` – Explanation-related functionality.
- `quiz_module.py` – Quiz-related functionality.
- `learning_path.py` – Learning-path functionality.
- `summary_module.py` – Summary-related functionality.
- `models.py` – Application data models.
- `prompts.py` – AI prompt definitions.
- `templates/` – Application templates.
- `static/` – Static assets.

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd EduGenie-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements
```

If your project uses a different requirements filename, use the corresponding file.

### 4. Configure environment variables

Create a `.env` file based on `.env.example` and add the required configuration values.

**Do not upload `.env` or API keys to GitHub.**

### 5. Run the application

Use the project's configured entry point:

```bash
python main.py
```

## Documentation

Detailed documentation is available in the `docs/` folder:

- [Project Overview](docs/project-overview.md)
- [Features](docs/features.md)
- [Installation](docs/installation.md)
- [Project Structure](docs/project-structure.md)
- [User Guide](docs/user-guide.md)

## Security

Keep API keys, passwords, tokens, and other secrets in environment variables. Never commit secret values to a public repository.

## License

Add your project's license information here.
