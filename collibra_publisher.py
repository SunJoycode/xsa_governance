import requests
from app.config import COLLIBRA_URL, COLLIBRA_TOKEN

def publish_collibra(asset):

    if not COLLIBRA_URL:
        return "Collibra URL not configured"

    url = f"{COLLIBRA_URL}/assets"

    headers = {
        "Authorization": f"Bearer {COLLIBRA_TOKEN}"
    }

    payload = {
        "name": asset["name"],
        "type": "Data Product",
        "description": asset["description"]
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.status_code
