import asyncio
import os
from check_logic import perform_price_check
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID   = int(os.getenv("CHAT_ID"))

async def main():
    print("▶️ Starting hourly_checker")
    msg, _ = perform_price_check()
    print("📝 Built message:", msg.replace("\n", "\\n"))
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=msg)
        print("✅ Message sent to Telegram")
    except Exception as e:
        print("❌ Error sending message:", e)

if __name__ == "__main__":
    asyncio.run(main())
