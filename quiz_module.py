def generate_quiz(
    topic: str,
    subject: str = "General",
    number_of_questions: int = 5,
    difficulty: str = "medium",
    language: str = "English",
):
    questions = []

    for i in range(1, number_of_questions + 1):
        questions.append(
            {
                "question_number": i,
                "question": f"Sample question {i} about {topic}",
                "options": [
                    "Option A",
                    "Option B",
                    "Option C",
                    "Option D",
                ],
                "answer": "Option A",
            }
        )

    return {
        "success": True,
        "topic": topic,
        "subject": subject,
        "difficulty": difficulty,
        "language": language,
        "questions": questions,
    }