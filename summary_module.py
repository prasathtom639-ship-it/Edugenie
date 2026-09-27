from typing import Dict, Any


def generate_summary(
    text: str,
    language: str = "English",
    max_length: int = 500
) -> Dict[str, Any]:
    """
    Generate a simple summary from the provided text.
    """

    text = text.strip()

    if not text:
        return {
            "success": False,
            "summary": "Please provide some text to summarize.",
            "language": language,
        }

    # Simple local fallback summary.
    # AI-powered summarization can be connected later.
    words = text.split()

    if len(words) <= 80:
        summary = text
    else:
        summary = " ".join(words[:80]) + "..."

    if max_length and len(summary) > max_length:
        summary = summary[:max_length].rsplit(" ", 1)[0] + "..."

    return {
        "success": True,
        "summary": summary,
        "language": language,
        "original_length": len(text),
        "summary_length": len(summary),
    }