import time
from xdk.oauth2_auth import OAuth2PKCEAuth
from config import X_CLIENT_ID, X_CLIENT_SECRET

redirect_uri = "http://localhost:8080/callback"
scopes = ["tweet.read", "tweet.write", "users.read", "offline.access"]


def main_auth():
    auth = OAuth2PKCEAuth(
        client_id=X_CLIENT_ID,
        client_secret=X_CLIENT_SECRET,
        redirect_uri=redirect_uri,
        scope=scopes,
    )

    auth_url = auth.get_authorization_url()
    print("Authorize here:")
    print(auth_url)

    callback_url = input("Paste callback URL: ")

    tokens = auth.fetch_token(authorization_response=callback_url)

    return {
        "access_token": tokens["access_token"],
        "refresh_token": tokens.get("refresh_token"),
        "expires_at": time.time() + tokens["expires_in"] - 60,
    }


if __name__ == "__main__":
    auth_data = main_auth()
    print("\n=== TOKENS GENERATED ===\n")
    for k, v in auth_data.items():
        print(f"{k}: {v}")
