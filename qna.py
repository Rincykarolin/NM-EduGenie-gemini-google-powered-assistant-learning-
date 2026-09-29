from gemini_client import generate_text


async def answer_question(
    question: str
):

    prompt = f"""
You are EduGenie, an educational
question-answering assistant.

Answer this student question:

{question}

Rules:

1. Give the direct answer first.
2. Explain the reasoning or context briefly.
3. Use simple educational language.
4. If the question is ambiguous,
   explain the ambiguity.
5. Do not invent facts.
6. Do not claim certainty when
   information is uncertain.
7. Make the answer useful for learning.
"""

    answer = await generate_text(
        prompt
    )

    return {
        "question": question,
        "answer": answer
    }