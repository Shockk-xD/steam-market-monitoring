# hourly_checker.py
import os
from check_logic import perform_price_check
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID   = int(os.getenv("CHAT_ID"))

if __name__ == "__main__":
    msg, _ = perform_price_check()
    Bot(token=BOT_TOKEN).send_message(chat_id=CHAT_ID, text=msg)
