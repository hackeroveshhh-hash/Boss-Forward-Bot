# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio, logging
from config import Config
from pyrogram import Client as VJ, idle
from typing import Union, Optional, AsyncGenerator
from logging.handlers import RotatingFileHandler
from plugins.regix import restart_forwards

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=5000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    VJBot = VJ(
        "VJ-Forward-Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=dict(root="plugins")
    )  

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1
               
    async def main():
        await VJBot.start()
        bot_info = await VJBot.get_me()
        
        # Small Caps Log Implementation [cite: 2025-12-23]
        restart_msg = (
            f"⚡ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✨\n\n"
            f"👤 ɴᴀᴍᴇ: {bot_info.first_name}\n"
            f"🆔 ɪᴅ: `{bot_info.id}`\n"
            f"🌐 sᴇʀᴠᴇʀ: ʀᴇɴᴅᴇʀ ᴀᴅᴠᴀɴᴄᴇᴅ\n"
            f"📅 sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ & ʀᴇᴀᴅʏ"
        )
        
        try:
            # Sending log to your specific channel [cite: 2025-12-23]
            await VJBot.send_message(Config.LOG_ID, restart_msg)
        except Exception as e:
            print(f"Log Error: {e}")

        await restart_forwards(VJBot)
        print(f"@{bot_info.username} Started Successfully!")
        await idle()

    asyncio.get_event_loop().run_until_complete(main())

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
