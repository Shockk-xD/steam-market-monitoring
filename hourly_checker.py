import asyncio
import os
from check_logic import perform_price_check
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

async def main():
    msg, _ = perform_price_check()
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=msg)  # ВАЖНО: await

if __name__ == "__main__":
    asyncio.run(main())
