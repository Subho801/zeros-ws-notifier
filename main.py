from websocket_client import fetch_current_giveaway
from discord import send_discord
from state import load_state, save_state

state = load_state()
posted = set(state["posted"])

giveaway = fetch_current_giveaway()

# Unique event for each status
event_id = f"{giveaway['id']}_{giveaway['status']}"

if event_id in posted:
    print(f"Already posted ({giveaway['status']}).")
else:
    send_discord(giveaway)

    posted.add(event_id)

    state["posted"] = list(posted)

    save_state(state)

    print(f"Posted ({giveaway['status']})!")