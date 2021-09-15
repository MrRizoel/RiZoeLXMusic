from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2

RIZ_MSG = """
◑ ━━━━━ ▣ ━━━━━ ◐
➣ ʙᴏᴛ ᴠɪʀsɪᴏɴ : 1.0.2
➣ ᴄʀᴇᴀᴛᴏʀ : [ʀɪᴢᴏᴇʟ](https://t.me/TheRiZoeL)
➣ sᴜᴘᴘᴏʀᴛ : [ᴊᴏɪɴ](https://t.me/DNHxHELL)
➣ sᴛᴀʀᴛ ᴛɪᴍᴇ : 
➣ ᴜᴘᴛɪᴍᴇ :
◑ ━━━━━ ▣ ━━━━━ ◐"""

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAELUCJhGiacm9ro5nAJXr_GlzPrpV3UgAACNwIAAkGdiFW9ustLyOBHoiAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I'm Private music of @TheRiZoeL For group's voice call. Developed by [ℝ𝚒ℤ𝚘𝚎𝕃](https://t.me/TheRiZoeL).

If you want to add this Bot in your group Contact @TheRiZoeL**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀ℝ𝚒ℤ𝚘𝚎𝕃", url="https://t.me/TheRiZoeL")
                  ],[ 
                    InlineKeyboardButton(
                        "ᴅɴʜxʜᴇʟʟ", url="https://t.me/DNHxHELL"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**RiZoeL Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "RiZoeL", url="https://t.me/RiZoeL")
                ]
            ]
        )
   )


RIZ_PIC = "https://telegra.ph/file/d9f9d87cf08142a8cafe2.jpg"
@Client.on_message(filters.command("alive") & ~filters.edited)
async def alive(client: Client, message: Message):
    if RIZ_PIC:
       caption=RIZ_MSG,
       reply_markup=InlineKeyboardMarkup(                   
                          [[
                              InlineKeyboardButton(
            text="🥀ℝ𝚒ℤ𝚘𝚎𝕃", url="http://t.me/TheRiZoeL"),
                          ]]
