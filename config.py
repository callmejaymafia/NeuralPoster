import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
X_CLIENT_ID = os.getenv("X_CLIENT_ID")
X_CLIENT_SECRET = os.getenv("X_CLIENT_SECRET")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API = os.getenv("OPENROUTER_API")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

if not all(
    [
        TELEGRAM_BOT_TOKEN,
        X_CLIENT_ID,
        X_CLIENT_SECRET,
        X_ACCESS_TOKEN_SECRET,
        X_ACCESS_TOKEN,
        GROQ_API_KEY,
    ]
):
    missing = [
        name
        for name, value in {
            "TELEGRAM_BOT_TOKEN": TELEGRAM_BOT_TOKEN,
            "X_CLIENT_ID": X_CLIENT_ID,
            "X_CLIENT_SECRET": X_CLIENT_SECRET,
            "GROQ_API_KEY": GROQ_API_KEY,
            "OPENROUTER_API": OPENROUTER_API,
            "X_ACCESS_TOKEN": X_ACCESS_TOKEN,
            "X_ACCESS_TOKEN_SECRET": X_ACCESS_TOKEN_SECRET,
        }.items()
        if not value
    ]
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")
