# hourly_checker.py
import os
from telegram import Bot
from check_logic import perform_price_check

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise Exception("❌ BOT_TOKEN или CHAT_ID не заданы!")

msg = perform_price_check()
bot = Bot(token=BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text=msg)
