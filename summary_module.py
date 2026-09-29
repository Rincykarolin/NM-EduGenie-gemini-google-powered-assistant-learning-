from gemini_client import generate_text


async def summarize_text(
    text: str
):

    prompt = f"""
You are EduGenie.

Summarize this educational passage:

{text}

Requirements:

1. Preserve the main information.
2. Remove unnecessary repetition.
3. Use simple language.
4. Make it useful for revision.
5. Include a short summary.
6. Include 3 to 7 important key points.
7. Do not add information that
   is not supported by the passage.
"""

    summary = await generate_text(
        prompt
    )

    return {
        "summary": summary
    }