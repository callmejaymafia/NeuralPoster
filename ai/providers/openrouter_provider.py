import httpx
from config import OPENROUTER_API

MODEL = "openai/gpt-oss-120b:free"


async def generate_text(user_prompt: str, system_prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }

    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=payload,
            headers=headers,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
