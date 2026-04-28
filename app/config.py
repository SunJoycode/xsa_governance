import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

COLLIBRA_URL = os.getenv("COLLIBRA_URL")
COLLIBRA_TOKEN = os.getenv("COLLIBRA_TOKEN")

ELLIE_URL = os.getenv("ELLIE_URL")
ELLIE_TOKEN = os.getenv("ELLIE_TOKEN")
