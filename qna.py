from typing import Dict, Any


def answer_question(
    question: str,
    subject: str = "General",
    language: str = "English"
) -> Dict[str, Any]:
    """
    Answer a student's question.

    This is a simple local fallback implementation.
    It allows the FastAPI application to run even when
    an external AI API is not configured.
    """

    question = question.strip()

    if not question:
        return {
            "success": False,
            "question": "",
            "answer": "Please enter a question.",
            "subject": subject,
            "language": language,
        }

    answer = (
        f"EduGenie Q&A\n\n"
        f"Question: {question}\n\n"
        f"Subject: {subject}\n"
        f"Language: {language}\n\n"
        "Please configure the AI provider in your .env file "
        "to generate an AI-powered answer."
    )

    return {
        "success": True,
        "question": question,
        "answer": answer,
        "subject": subject,
        "language": language,
    }