from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import (
    QARequest,
    ExplainRequest,
    QuizRequest,
    SummaryRequest,
    LearningPathRequest,
)

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import generate_summary
from learning_path import get_learning_recommendations

app = FastAPI(
    title="EduGenie AI",
    description="AI-powered learning assistant",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "EduGenie AI is running successfully!",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/qa")
def qa(request: QARequest):
    return answer_question(
        question=request.question,
        subject=request.subject,
        language=request.language,
    )


@app.post("/api/explain")
def explain(request: ExplainRequest):
    return explain_topic(
        topic=request.topic,
        subject=request.subject,
        language=request.language,
    )


@app.post("/api/quiz")
def quiz(request: QuizRequest):
    return generate_quiz(
        topic=request.topic,
        subject=request.subject,
        number_of_questions=request.number_of_questions,
        difficulty=request.difficulty,
        language=request.language,
    )


@app.post("/api/summary")
def summary(request: SummaryRequest):
    return generate_summary(
        text=request.text,
        language=request.language,
    )


@app.post("/api/learning-path")
def learning_path(request: LearningPathRequest):
    return get_learning_recommendations(
        subject=request.subject,
        level=request.level,
        goal=request.goal,
        language=request.language,
    )