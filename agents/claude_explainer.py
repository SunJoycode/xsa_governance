import anthropic
from app.config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY
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

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1500,
        temperature=0.2,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text
