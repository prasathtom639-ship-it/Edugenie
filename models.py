from pydantic import BaseModel, Field
from typing import List, Optional


class QARequest(BaseModel):
    question: str = Field(..., min_length=1)
    subject: str = "General"
    language: str = "English"


class ExplainRequest(BaseModel):
    topic: str = Field(..., min_length=1)
    subject: str = "General"
    language: str = "English"
    level: str = "College"


class QuizRequest(BaseModel):
    topic: str = Field(..., min_length=1)
    subject: str = "General"
    language: str = "English"
    num_questions: int = Field(default=5, ge=1, le=20)
    difficulty: str = "Medium"


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=1)
    language: str = "English"
    max_length: Optional[int] = 500


class LearningPathRequest(BaseModel):
    subject: str = Field(..., min_length=1)
    goal: str = Field(..., min_length=1)
    current_level: str = "Beginner"
    language: str = "English"


class APIError(BaseModel):
    detail: strss