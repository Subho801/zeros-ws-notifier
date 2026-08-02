import json
import re

from websocket import create_connection
from game_lookup import get_game_name

WS_URL = "ws://zeros.group:8863/"


def translate_title(title):
    title = title.strip()

    match = re.search(r"(\d+)月(\d+)日", title)

    if not match:
        return title

    month = int(match.group(1))
    day = int(match.group(2))

    months = [
        "",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    return f"{months[month]} {day} Event"


def format_rewards(rewards):
    formatted = []

    for reward in rewards:
        reward = reward.strip('" ,')

        # Skip headers and notices
        if (
            "必看" in reward
            or "请注意" in reward
            or not reward
        ):
            continue

        reward = reward.replace("✖", "×")

        # Remove price tag like [108￥]
        reward = re.sub(r"\[\d+￥\]\s*", "", reward)

        match = re.match(r"(.+?)\s*×\s*(\d+)", reward)

        if not match:
            continue

        chinese_name = match.group(1).strip()
        quantity = match.group(2)

        english_name = get_game_name(chinese_name)

        formatted.append(f"• {english_name} × {quantity}")

    return "\n".join(formatted[:6])


def fetch_current_giveaway():
    ws = create_connection(
        WS_URL,
        origin="http://zeros.group"
    )

    try:
        ws.send("getConfig")
        response = ws.recv()
    finally:
        ws.close()

    if not response.startswith("config "):
        raise RuntimeError(f"Unexpected response: {response}")

    data = json.loads(response[len("config "):])

    activity = data["activity"]
    current_period = activity["period_id"]

    current = next(
        p for p in data["periods"]
        if p["period_id"] == current_period
    )

    stock = current.get("stock_count", 0)
    claimed = current.get("claim_count", 0)
    total = stock + claimed

    if current["is_expired"]:
        status = "Expired"
    elif current["is_not_started"]:
        status = "Upcoming"
    elif stock > 0:
        status = "Live"
    else:
        # Safety fallback
        status = "Upcoming"
        
    print(json.dumps(current, indent=2, ensure_ascii=False))
    
    return {
        "id": current["period_id"],
        "title": "Random Steam Key Giveaway",
        "period_name": translate_title(current["period_name"]),
        "reward": current["reward_desc"]
            .replace("随机游戏激活码", "Random Steam Key")
            .replace("✖", " × "),
        "deadline": current["deadline"],
        "start_time": current["start_time"],
        "image": "http://zeros.group/free/random.jpg",
        "stock": stock,
        "claimed": claimed,
        "total": total,
        "status": status,
        "games": current.get("games", []),
        "featured_rewards": format_rewards(
            current.get("rewards_content", [])
        ),
    }


if __name__ == "__main__":
    giveaway = fetch_current_giveaway()

    print(json.dumps(giveaway, indent=2, ensure_ascii=False))
