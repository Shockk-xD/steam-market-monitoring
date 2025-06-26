# hourly_checker.py
# -*- coding: utf-8 -*-
from check_logic import perform_price_check
from telegram import Bot

BOT_TOKEN = '7700315955:AAFqi6Bat6VFNoVTLEFKZo4Ac1WD8ROyv3Y'
CHAT_ID   = 1085776764

if __name__ == "__main__":
    msg, _ = perform_price_check()
    Bot(token=BOT_TOKEN).send_message(chat_id=CHAT_ID, text=msg)
