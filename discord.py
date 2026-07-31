import os
import requests
from datetime import datetime, timedelta, timezone

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

FOOTER_ICON = "https://files.catbox.moe/qttqpy.png"

CHINA_TZ = timezone(timedelta(hours=8))


def discord_timestamp(iso_time, style="R"):
    dt = datetime.fromisoformat(iso_time)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=CHINA_TZ)

    return f"<t:{int(dt.timestamp())}:{style}>"
    


def send_discord(item):
    if not WEBHOOK_URL:
        raise RuntimeError("DISCORD_WEBHOOK_URL missing")

    colors = {
    "Upcoming": 0xFEE75C,   # Yellow
    "Live": 0x57F287,       # Green
    "Expired": 0xED4245,    # Red
}
    icons = {
    "Upcoming": "🟡",
    "Live": "🟢",
    "Expired": "🔴",
}
    embed = {
        "author": {
        "name": "Zeros Group - Giveaways",
        "icon_url": "https://file.garden/afbSsuts32dZ5wSl/El-Gato-Cat-Adorable-Cartoon-Cat-PNG-thumb.png"
    },
    "title": f"🎁 {item['title']}",
    "url": "https://zeros.group/free/",
    "color": colors[item["status"]],
    "fields": [
        {
            "name": "Status",
            "value": f"{icons[item['status']]} {item['status']}",
            "inline": True,
        },
        {
            "name": "Keys",
            "value": f"🔑 {item['stock']} / {item['claimed']}",
            "inline": True,
        },
        {
            "name": "Deadline",
            "value": f"⏳ {discord_timestamp(item['deadline'])}",
            "inline": True,
        },
        {
            "name": "🏆 Featured Rewards",
            "value": item["featured_rewards"] or "None",
            "inline": False,
        },
    ],
    "footer": {
        "text": "Subho's Zeros Group Notifier",
        "icon_url": FOOTER_ICON,
    },
}

    if item["image"]:
        embed["image"] = {
            "url": item["image"]
        }

    requests.post(
        WEBHOOK_URL,
        json={"embeds": [embed]},
        timeout=30
    ).raise_for_status()
