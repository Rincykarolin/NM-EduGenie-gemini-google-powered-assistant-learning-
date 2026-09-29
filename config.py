import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseModel, Field


load_dotenv()


class Settings(BaseModel):

    app_name: str = Field(
        default="EduGenie"
    )

    environment: str = Field(
        default="development"
    )

    gemini_api_key: str = Field(
        default=""
    )

    gemini_model: str = Field(
        default="gemini-3.8-flash"
    )

    local_explanation_model: str = Field(
        default="MBZUAI/LaMini-Flan-T5-783M"
    )

    use_local_explanation: bool = Field(
        default=False
    )

    max_input_chars: int = Field(
        default=20000,
        ge=1000,
        le=100000
    )

    cors_origins: str = Field(
        default="*"
    )

    @property
    def cors_origin_list(self):
        return [
            item.strip()
            for item in self.cors_origins.split(",")
            if item.strip()
        ]


@lru_cache
def get_settings():

    return Settings(

        app_name=os.getenv(
            "APP_NAME",
            "EduGenie"
        ),

        environment=os.getenv(
            "ENVIRONMENT",
            "development"
        ),

        gemini_api_key=os.getenv(
            "GEMINI_API_KEY",
            ""
        ),

        gemini_model=os.getenv(
            "GEMINI_MODEL",
            "gemini-3.8-flash"
        ),

        local_explanation_model=os.getenv(
            "LOCAL_EXPLANATION_MODEL",
            "MBZUAI/LaMini-Flan-T5-783M"
        ),

        use_local_explanation=os.getenv(
            "USE_LOCAL_EXPLANATION",
            "false"
        ).lower() in {
            "1",
            "true",
            "yes",
            "on"
        },

        max_input_chars=int(
            os.getenv(
                "MAX_INPUT_CHARS",
                "20000"
            )
        ),

        cors_origins=os.getenv(
            "CORS_ORIGINS",
            "*"
        )
    )