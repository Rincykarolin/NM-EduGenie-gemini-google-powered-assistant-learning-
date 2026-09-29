from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import (
    ExplainRequest,
    LearningPathRequest,
    QARequest,
    QuizRequest,
    SummaryRequest,
)

from explanation_module import explain_concept
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)


# Static files
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


# HTML templates
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# --------------------------------------------------
# Home
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "EduGenie"
    }


# --------------------------------------------------
# Question Answering
# --------------------------------------------------

@app.post("/qa")
async def qa(payload: QARequest):

    return await answer_question(
        payload.question
    )


# --------------------------------------------------
# Concept Explanation
# --------------------------------------------------

@app.post("/explain")
async def explain(payload: ExplainRequest):

    return await explain_concept(
        payload.topic,
        payload.level
    )


# --------------------------------------------------
# Quiz Generation
# --------------------------------------------------

@app.post("/quiz")
async def quiz(payload: QuizRequest):

    return await generate_quiz(
        payload.text,
        payload.topic
    )


# --------------------------------------------------
# Summarization
# --------------------------------------------------

@app.post("/summarize")
async def summarize(payload: SummaryRequest):

    return await summarize_text(
        payload.text
    )


# --------------------------------------------------
# Learning Recommendations
# --------------------------------------------------

@app.post("/learn/recommendations")
async def learning_recommendations(
    payload: LearningPathRequest
):

    return await get_learning_recommendations(
        payload.topic,
        payload.level
    )