# EduGenie Architecture

```text
Browser
   |
   | HTML/CSS/JavaScript
   v
FastAPI (main.py)
   |
   +--> /qa ----------------------> qna.py
   |
   +--> /explain -----------------> explanation_module.py
   |                                  |
   |                                  +--> Gemini (default)
   |                                  |
   |                                  +--> LaMini-Flan-T5 (optional)
   |
   +--> /quiz --------------------> quiz_module.py
   |
   +--> /summarize ---------------> summary_module.py
   |
   +--> /learn/recommendations ---> learning_path.py
                                      |
                                      v
                                gemini_client.py
                                      |
                                      v
                              Google Gemini API

Shared:
- config.py       environment/configuration
- models.py       request/response validation
- templates/      web UI
- static/         CSS
- tests/          automated API/model validation
```

## Data flow

1. Student submits a task in the browser.
2. JavaScript selects the corresponding FastAPI endpoint.
3. Pydantic validates the request.
4. The relevant module builds an educational prompt.
5. `gemini_client.py` calls Gemini.
6. Structured responses are validated with Pydantic for quiz and learning-path operations.
7. FastAPI returns JSON.
8. The browser renders the result.
