from models import QuizResponse
from gemini_client import generate_structured


async def generate_quiz(
    text: str = "",
    topic: str = ""
):

    if text:

        source = text

    else:

        source = f"Topic: {topic}"

    prompt = f"""
Create an educational multiple-choice
quiz using this source:

SOURCE:

{source}

Requirements:

1. Generate exactly 3 questions.
2. Every question must have exactly
   4 options.
3. There must be exactly one correct answer.
4. The answer must exactly match one
   of the option strings.
5. Give a short explanation.
6. Questions must be educational.
7. When a passage is provided,
   do not rely on unrelated information.
8. Avoid ambiguous questions.
"""

    result = await generate_structured(
        prompt,
        QuizResponse
    )

    return result.model_dump()