# check_logic.py
# -*- coding: utf-8 -*-
import json
import os
import urllib.parse
import requests

SKINS_FILE   = "skins.json"
RECORDS_FILE = "records.json"

def load_skins():
    if not os.path.exists(SKINS_FILE):
        return []
    with open(SKINS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_records():
    if not os.path.exists(RECORDS_FILE):
        return {}
    with open(RECORDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_records(records):
    with open(RECORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

def perform_price_check():
    skins   = load_skins()
    records = load_records()
    msg     = "💰 Проверка цен:\n\n"

    for skin_url in skins:
        try:
            market_name  = skin_url.split("/")[-1]
            decoded_name = urllib.parse.unquote(market_name)
            url          = (
                "https://steamcommunity.com/market/priceoverview/"
                f"?country=US&currency=1&appid=730&market_hash_name={decoded_name}"
            )
            data = requests.get(url, timeout=5).json()

            if data.get("success") and data.get("lowest_price"):
                price_str = data["lowest_price"].replace("$", "").replace(",", ".").strip()
                price     = float(price_str)
                old_rec   = records.get(skin_url, 0)

                if price > old_rec:
                    records[skin_url] = price
                    msg += f"🔥 {decoded_name}: ${price:.2f} — НОВЫЙ РЕКОРД!\n"
                else:
                    msg += f"🔸 {decoded_name}: ${price:.2f}\n"
            else:
                msg += f"❓ {decoded_name}: цена не найдена\n"
        except Exception as e:
            msg += f"⚠️ Ошибка для {decoded_name}: {e}\n"

    save_records(records)
    return msg, records
