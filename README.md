# EduGenie

Google Gemini Powered Learning Assistant.

EduGenie is an AI-powered educational assistant that provides:

- Question answering
- Concept explanation
- Quiz generation
- Text summarization
- Personalized learning paths

## Technology Stack

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python
- FastAPI
- Uvicorn

AI:
- Google Gemini
- Optional LaMini-Flan-T5

Validation:
- Pydantic

Testing:
- Pytest


# Folder Structure

EduGenie/

├── main.py
├── config.py
├── models.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── tests/
│   ├── test_api.py
│   └── test_models.py
│
└── .vscode/


# Installation

## Step 1

Install Python 3.10 or newer.

Check:

python --version


## Step 2

Open the EduGenie folder in VS Code.


## Step 3

Open:

Terminal → New Terminal


## Step 4

Create virtual environment.

Windows:

python -m venv .venv


Activate:

.\.venv\Scripts\Activate.ps1


If PowerShell activation does not work:

.venv\Scripts\activate


## Step 5

Install dependencies:

pip install --upgrade pip

pip install -r requirements.txt


# Gemini API Key

Create a .env file.

Example:

GEMINI_API_KEY=your_api_key_here

GEMINI_MODEL=gemini-3.8-flash

USE_LOCAL_EXPLANATION=false


# Run Application

Run:

uvicorn main:app --reload


Open browser:

http://127.0.0.1:8000


# API Documentation

FastAPI automatically provides:

http://127.0.0.1:8000/docs


Alternative:

http://127.0.0.1:8000/redoc


# API Endpoints

GET /health

POST /qa

POST /explain

POST /quiz

POST /summarize

POST /learn/recommendations


# Example Q&A

POST /qa

{
    "question": "Which is the largest ocean?"
}


# Example Explanation

POST /explain

{
    "topic": "Pythagoras theorem",
    "level": "beginner"
}


# Example Quiz

POST /quiz

{
    "topic": "Photosynthesis"
}


# Example Summary

POST /summarize

{
    "text": "Photosynthesis is the process..."
}


# Example Learning Path

POST /learn/recommendations

{
    "topic": "SQL",
    "level": "beginner"
}


# Testing

Run:

pytest -q


# Health Check

Open:

http://127.0.0.1:8000/health


Expected:

{
    "status": "ok",
    "service": "EduGenie"
}


# Optional Local Explanation Model

The project documentation describes:

LaMini-Flan-T5-783M

as the local explanation model.

To enable it:

pip install transformers torch

Then change:

USE_LOCAL_EXPLANATION=true

The first run downloads the model.


# Important

Never publish your .env file.

Never put your Gemini API key inside JavaScript.

The API key belongs only in .env.


# Troubleshooting

If you see:

Gemini API key is not configured

check your .env file.


If you see:

ModuleNotFoundError

run:

pip install -r requirements.txt


If the server does not start:

check:

python --version


and:

pip show fastapi


# Development

Run:

uvicorn main:app --reload


# Production

For deployment, configure:

- environment variables
- HTTPS
- restricted CORS
- authentication
- rate limiting
- logging
- secure secret management