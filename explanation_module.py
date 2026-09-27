from typing import Dict, Any


def explain_topic(
    topic: str,
    subject: str = "General",
    language: str = "English",
    level: str = "College"
) -> Dict[str, Any]:
    """
    Generate a simple explanation for a given topic.
    """

    topic = topic.strip()

    if not topic:
        return {
            "success": False,
            "topic": "",
            "explanation": "Please enter a topic.",
            "subject": subject,
            "language": language,
            "level": level,
        }

    explanation = (
        f"EduGenie Explanation\n\n"
        f"Topic: {topic}\n"
        f"Subject: {subject}\n"
        f"Level: {level}\n"
        f"Language: {language}\n\n"
        f"{topic} is an important topic in {subject}. "
        f"This topic can be understood by learning its basic definition, "
        f"main concepts, important features, examples, and applications.\n\n"
        "Configure your AI provider in the .env file to generate "
        "a detailed AI-powered explanation."
    )

    return {
        "success": True,
        "topic": topic,
        "explanation": explanation,
        "subject": subject,
        "language": language,
        "level": level,
    }