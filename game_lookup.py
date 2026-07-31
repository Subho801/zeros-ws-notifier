import json
import os

from deep_translator import GoogleTranslator
from igdb import lookup_game_name

CACHE_FILE = "game_cache.json"


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def translate_fallback(text):
    try:
        return GoogleTranslator(
            source="zh-CN",
            target="en"
        ).translate(text)
    except Exception:
        return text


def get_game_name(chinese_name):
    cache = load_cache()

    if chinese_name in cache:
        return cache[chinese_name]

    english = lookup_game_name(chinese_name)

    if english:
        cache[chinese_name] = english
    else:
        cache[chinese_name] = "Random Steam Game"

    save_cache(cache)

    return cache[chinese_name]

if __name__ == "__main__":
    print(get_game_name("幻兽帕鲁"))
    print(get_game_name("黑神话：悟空"))
    print(get_game_name("盘丝洞惊魂"))