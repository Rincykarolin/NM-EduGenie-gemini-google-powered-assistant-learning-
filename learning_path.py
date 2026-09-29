from models import LearningPathResponse

from gemini_client import generate_structured


async def get_learning_recommendations(
    topic: str,
    level: str = "beginner"
):

    prompt = f"""
Create a structured learning path
for:

Topic: {topic}

Learner level: {level}

Requirements:

1. Start with fundamentals.
2. Progress toward intermediate concepts.
3. Finish with advanced concepts.
4. Organize the topics logically.
5. Provide suggested study time.
6. Provide useful resource types.
7. Include practice activities where appropriate.
8. Make the plan realistic for self-learning.
9. Do not invent exact URLs.
"""

    result = await generate_structured(
        prompt,
        LearningPathResponse
    )

    result.topic = topic
    result.level = level

    return result.model_dump()