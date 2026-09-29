from functools import lru_cache
from typing import TypeVar

from fastapi import HTTPException
from google import genai
from google.genai import types
from pydantic import BaseModel

from config import get_settings


T = TypeVar(
    "T",
    bound=BaseModel
)


# --------------------------------------------------
# Gemini Client
# --------------------------------------------------

@lru_cache
def get_client():

    settings = get_settings()

    if not settings.gemini_api_key:

        raise HTTPException(
            status_code=503,
            detail=(
                "Gemini API key is not configured. "
                "Please add GEMINI_API_KEY to .env."
            )
        )

    return genai.Client(
        api_key=settings.gemini_api_key
    )


# --------------------------------------------------
# Text Generation
# --------------------------------------------------

async def generate_text(
    prompt: str,
    temperature: float = 0.4
):

    settings = get_settings()

    client = get_client()

    try:

        response = client.models.generate_content(

            model=settings.gemini_model,

            contents=prompt,

            config=types.GenerateContentConfig(

                temperature=temperature,

                max_output_tokens=2048
            )
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=f"Gemini API request failed: {exc}"
        ) from exc

    text = (
        response.text or ""
    ).strip()

    if not text:

        raise HTTPException(
            status_code=502,
            detail="Gemini returned an empty response."
        )

    return text


# --------------------------------------------------
# Structured Generation
# --------------------------------------------------

async def generate_structured(
    prompt: str,
    schema: type[T],
    temperature: float = 0.2
) -> T:

    settings = get_settings()

    client = get_client()

    try:

        response = client.models.generate_content(

            model=settings.gemini_model,

            contents=prompt,

            config=types.GenerateContentConfig(

                temperature=temperature,

                max_output_tokens=4096,

                response_mime_type="application/json",

                response_schema=schema
            )
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=f"Gemini API request failed: {exc}"
        ) from exc

    text = (
        response.text or ""
    ).strip()

    if not text:

        raise HTTPException(
            status_code=502,
            detail=(
                "Gemini returned an empty "
                "structured response."
            )
        )

    try:

        return schema.model_validate_json(
            text
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=(
                "Gemini returned invalid "
                f"structured data: {exc}"
            )
        ) from exc