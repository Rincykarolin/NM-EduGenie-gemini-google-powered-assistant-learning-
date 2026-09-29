from fastapi import HTTPException

from config import get_settings
from gemini_client import generate_text


def local_explanation(
    topic: str,
    level: str
):

    try:

        from transformers import pipeline

    except ImportError as exc:

        raise HTTPException(
            status_code=500,
            detail=(
                "Local explanation requires "
                "transformers. Install the optional "
                "local-model dependencies or use "
                "USE_LOCAL_EXPLANATION=false."
            )
        ) from exc

    settings = get_settings()

    try:

        generator = pipeline(
            "text2text-generation",
            model=settings.local_explanation_model
        )

        prompt = f"""
Explain {topic} to a {level} learner
using very simple language.

Include:

1. Simple definition
2. Main idea
3. Three important points
4. One easy example

Keep the explanation concise.
"""

        result = generator(
            prompt,
            max_new_tokens=220,
            do_sample=False
        )

        return result[0][
            "generated_text"
        ].strip()

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=(
                f"Local explanation model failed: {exc}"
            )
        ) from exc


async def explain_concept(
    topic: str,
    level: str = "beginner"
):

    settings = get_settings()

    if settings.use_local_explanation:

        answer = local_explanation(
            topic,
            level
        )

        provider = "LaMini-Flan-T5"

    else:

        prompt = f"""
You are EduGenie, an educational assistant.

Explain:

{topic}

Learner level:

{level}

Requirements:

- Start with a simple definition.
- Explain the core idea.
- Use simple educational language.
- Include an easy example.
- Avoid unnecessary jargon.
- Keep it concise.
"""

        answer = await generate_text(
            prompt
        )

        provider = "Gemini"

    return {

        "topic": topic,

        "level": level,

        "answer": answer,

        "provider": provider
    }