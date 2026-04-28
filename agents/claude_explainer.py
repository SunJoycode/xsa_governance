from openai import OpenAI
from app.config import GITHUB_TOKEN

client = OpenAI(
    api_key=GITHUB_TOKEN,
    base_url="https://models.inference.ai.azure.com"
)

def explain_logic(sql_code):

    prompt = f"""
Explain this HANA SQLScript logic.

Return:

- Business Purpose
- Tables Used
- Metrics
- Formula
- Suggested Data Product

SQL:
{sql_code}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=1500,
        temperature=0.2,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
