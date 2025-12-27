import json
import time
import httpx
from config import X_CLIENT_ID, X_CLIENT_SECRET

AUTH_FILE = "x_auth.json"
TOKEN_URL = "https://api.x.com/2/oauth2/token"


def load_auth():
    """Load tokens from JSON file."""
    with open(AUTH_FILE, "r") as f:
        return json.load(f)


def save_auth(auth):
    """Save tokens to JSON file."""
    with open(AUTH_FILE, "w") as f:
        json.dump(auth, f, indent=2)


def is_expired(auth):
    """Check if the access token is expired."""
    return time.time() >= auth["expires_at"]


async def refresh_access_token(auth):
    """Refresh the access token using the refresh token."""
    data = {
        "grant_type": "refresh_token",
        "refresh_token": auth["refresh_token"],
        "client_id": X_CLIENT_ID,
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    auth_basic = (X_CLIENT_ID, X_CLIENT_SECRET)

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(
            TOKEN_URL,
            data=data,
            headers=headers,
            auth=auth_basic,
        )
    response.raise_for_status()
    tokens = response.json()

    auth["access_token"] = tokens["access_token"]
    auth["expires_at"] = time.time() + tokens["expires_in"] - 60

    if "refresh_token" in tokens:
        auth["refresh_token"] = tokens["refresh_token"]

    save_auth(auth)
    return auth


async def get_valid_access_token():
    """Get a valid access token, refreshing if necessary."""
    auth = load_auth()

    if is_expired(auth):
        auth = await refresh_access_token(auth)

    return auth["access_token"]
