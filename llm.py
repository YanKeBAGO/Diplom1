import ollama
from config import LLM_MODEL


def generate_llm_analysis(summary):

    prompt = f"""
Проанализируй психолингвистические показатели диалога:

{summary}

Сделай академический вывод о характере отношений,
уровне конфликтности и психологической динамике.
Не анализируй отдельные фразы.
Дай общий профессиональный вывод.
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.2}
    )

    return response["message"]["content"]
