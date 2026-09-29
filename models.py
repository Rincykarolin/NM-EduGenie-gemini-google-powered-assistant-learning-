from pydantic import BaseModel, Field, field_validator


MAX_TEXT = 20000


# --------------------------------------------------
# Q&A
# --------------------------------------------------

class QARequest(BaseModel):

    question: str = Field(
        min_length=2,
        max_length=MAX_TEXT
    )

    @field_validator("question")
    @classmethod
    def validate_question(cls, value):

        value = value.strip()

        if not value:
            raise ValueError(
                "Question cannot be empty."
            )

        return value


# --------------------------------------------------
# Explanation
# --------------------------------------------------

class ExplainRequest(BaseModel):

    topic: str = Field(
        min_length=2,
        max_length=MAX_TEXT
    )

    level: str = Field(
        default="beginner",
        max_length=50
    )

    @field_validator("topic")
    @classmethod
    def validate_topic(cls, value):

        value = value.strip()

        if not value:
            raise ValueError(
                "Topic cannot be empty."
            )

        return value


# --------------------------------------------------
# Quiz
# --------------------------------------------------

class QuizRequest(BaseModel):

    text: str = Field(
        default="",
        max_length=MAX_TEXT
    )

    topic: str = Field(
        default="",
        max_length=500
    )

    @field_validator("text", "topic")
    @classmethod
    def clean_fields(cls, value):

        return value.strip()

    def model_post_init(self, __context):

        if not self.text and not self.topic:

            raise ValueError(
                "Provide either text or topic."
            )


# --------------------------------------------------
# Summary
# --------------------------------------------------

class SummaryRequest(BaseModel):

    text: str = Field(
        min_length=1,
        max_length=MAX_TEXT
    )

    @field_validator("text")
    @classmethod
    def validate_text(cls, value):

        value = value.strip()

        if not value:
            raise ValueError(
                "Text cannot be empty."
            )

        return value


# --------------------------------------------------
# Learning Path
# --------------------------------------------------

class LearningPathRequest(BaseModel):

    topic: str = Field(
        min_length=2,
        max_length=500
    )

    level: str = Field(
        default="beginner",
        max_length=50
    )

    @field_validator("topic")
    @classmethod
    def validate_topic(cls, value):

        value = value.strip()

        if not value:
            raise ValueError(
                "Topic cannot be empty."
            )

        return value


# --------------------------------------------------
# Quiz Response
# --------------------------------------------------

class QuizQuestion(BaseModel):

    question: str

    options: list[str] = Field(
        min_length=4,
        max_length=4
    )

    answer: str

    explanation: str


class QuizResponse(BaseModel):

    title: str

    questions: list[QuizQuestion] = Field(
        min_length=1,
        max_length=10
    )


# --------------------------------------------------
# Learning Path Response
# --------------------------------------------------

class LearningStep(BaseModel):

    stage: str

    topics: list[str]

    suggested_time: str

    resources: list[str]


class LearningPathResponse(BaseModel):

    topic: str

    level: str

    goal: str

    steps: list[LearningStep]