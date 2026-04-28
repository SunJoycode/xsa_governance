import requests
from app.config import ELLIE_URL, ELLIE_TOKEN

def publish_ellie(model):

    if not ELLIE_URL or not ELLIE_TOKEN:
        print("Skipping Ellie — credentials not configured")
        return

    url = f"{ELLIE_URL}/models"

    headers = {
        "Authorization": f"Bearer {ELLIE_TOKEN}"
    }

    payload = {
        "name": model["name"],
        "description": model["description"]
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.status_code
