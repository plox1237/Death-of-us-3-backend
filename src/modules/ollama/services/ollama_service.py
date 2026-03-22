import requests
from dotenv import load_dotenv
import os

load_dotenv()
OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

async def ask_ollama(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 300
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)

    response.raise_for_status()

    data = response.json()
    return data.get("response", "").strip()