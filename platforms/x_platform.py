import httpx
from x_auth import get_valid_access_token

X_API_URL = "https://api.x.com/2/tweets"


async def post_tweet(text: str) -> str:
    # Always get a valid token (auto-refresh if needed)
    access_token = await get_valid_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(
            X_API_URL,
            json={"text": text},
            headers=headers,
        )

    response.raise_for_status()
    data = response.json()

    tweet_id = data["data"]["id"]
    return f"https://x.com/i/status/{tweet_id}"
