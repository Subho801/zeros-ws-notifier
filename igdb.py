import os
import requests

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

TOKEN_URL = "https://id.twitch.tv/oauth2/token"
IGDB_URL = "https://api.igdb.com/v4/games"


def get_access_token():
    if not CLIENT_ID or not CLIENT_SECRET:
        raise RuntimeError(
            "TWITCH_CLIENT_ID or TWITCH_CLIENT_SECRET is missing."
        )

    response = requests.post(
        TOKEN_URL,
        params={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "client_credentials",
        },
        timeout=20,
    )

    response.raise_for_status()

    return response.json()["access_token"]


def lookup_game_name(chinese_name):
    token = get_access_token()

    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }

    query = f'''
search "{chinese_name}";
fields name;
limit 1;
'''

    response = requests.post(
        IGDB_URL,
        headers=headers,
        data=query,
        timeout=20,
    )

    response.raise_for_status()

    games = response.json()

    if not games:
        return None

    return games[0]["name"]


if __name__ == "__main__":
    print(lookup_game_name("幻兽帕鲁"))
    print(lookup_game_name("黑神话：悟空"))
    print(lookup_game_name("盘丝洞惊魂"))