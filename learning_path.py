from typing import Dict, Any, List


def get_learning_recommendations(
    subject: str,
    goal: str,
    current_level: str = "Beginner",
    language: str = "English"
) -> Dict[str, Any]:
    """
    Generate a simple learning path for a student.
    """

    subject = subject.strip()
    goal = goal.strip()
    current_level = current_level.strip()

    if not subject or not goal:
        return {
            "success": False,
            "message": "Subject and goal are required.",
            "learning_path": []
        }

    learning_path: List[Dict[str, Any]] = [
        {
            "step": 1,
            "title": f"Introduction to {subject}",
            "description": f"Learn the basic concepts and terminology of {subject}."
        },
        {
            "step": 2,
            "title": "Core Concepts",
            "description": f"Study the important fundamental concepts required for {subject}."
        },
        {
            "step": 3,
            "title": "Practical Examples",
            "description": f"Practice examples and simple exercises related to {subject}."
        },
        {
            "step": 4,
            "title": "Advanced Topics",
            "description": f"Move from {current_level} level toward more advanced {subject} concepts."
        },
        {
            "step": 5,
            "title": "Project / Practice",
            "description": f"Build a small project or complete practical exercises to achieve the goal: {goal}."
        },
        {
            "step": 6,
            "title": "Revision and Assessment",
            "description": "Review the learned concepts and test your knowledge with quizzes and practice questions."
        }
    ]

    return {
        "success": True,
        "subject": subject,
        "goal": goal,
        "current_level": current_level,
        "language": language,
        "learning_path": learning_path
    }