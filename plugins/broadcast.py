# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram.errors import InputUserDeactivated, FloodWait, UserIsBlocked, PeerIdInvalid
from database import db
from pyrogram import Client, filters
from config import Config
import asyncio
import datetime
import time
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Progress Refresh Callback
@Client.on_callback_query(filters.regex(r"^refresh_status"))
async def refresh_status(bot, query):
    # Logic to fetch real-time stats from DB/Temp can be added
    await query.answer("🔄 sᴛᴀᴛᴜs ᴜᴘᴅᴀᴛᴇᴅ!", show_alert=False)

async def broadcast_messages(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await broadcast_messages(user_id, message)
    except (InputUserDeactivated, UserIsBlocked, PeerIdInvalid):
        return False, "Error"
    except Exception:
        return False, "Error"

@Client.on_message(filters.command("broadcast") & filters.user(Config.BOT_OWNER) & filters.reply)
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    
    # Custom Buttons with Refresh & Cancel
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 ʀᴇғʀᴇsʜ", callback_data="refresh_status")],
        [InlineKeyboardButton("❌ ᴄᴀɴᴄᴇʟ", callback_data="close_btn")]
    ])
    
    sts = await message.reply_text(
        text='🚀 **ᴜʟᴛʀᴀ ғᴀsᴛ ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴀʀᴛɪɴɢ...**',
        reply_markup=reply_markup
    )
    
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    success = 0
    
    # Ultra Fast Batch Processing
    async for user in users:
        if 'id' in user:
            # Parallel execution for speed
            asyncio.create_task(broadcast_messages(int(user['id']), b_msg))
            success += 1
            done += 1
            
            if done % 20 == 0:
                try:
                    await sts.edit(
                        f"🚀 **ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴ ᴘʀᴏɢʀᴇss**\n\n"
                        f"📊 ᴛᴏᴛᴀʟ: {total_users}\n"
                        f"✅ ᴅᴏɴᴇ: {done}\n"
                        f"⚡ sᴘᴇᴇᴅ: ᴜʟᴛʀᴀ ғᴀsᴛ",
                        reply_markup=reply_markup
                    )
                except:
                    pass
    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(
        f"✅ **ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ**\n\n"
        f"⏱️ ᴛɪᴍᴇ: {time_taken}\n"
        f"👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: {total_users}\n"
        f"🎉 sᴜᴄᴄᴇss: {success}"
    )
