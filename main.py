import os
from check_logic import perform_price_check
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

def main():
    print("▶️ Starting price check")
    msg, _ = perform_price_check()
    print("📝 Built message:", msg)

    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=msg)
    print("✅ Message sent to Telegram")

if __name__ == "__main__":
    main()
