from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from YTMUSIC import app
from config import BOT_USERNAME
from YTMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ ɴᴏʙɪᴛᴀ-ᴍᴜsɪᴄ ˼ ʙᴏᴛ ✪
 
 ❍ • ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ •
 
 ❍ • ᴘᴇʜʟᴇ ɴᴏʙɪᴛᴀ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ •
 
 ❍ • ᴄʜᴜᴘ ᴄʜᴀᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ❍ • ʀᴇᴘᴏ ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ •
 
 ❍ • ᴀɢʀ ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ ᴛᴏ ɴᴏʙɪᴛᴀ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
 ❍ • ɴᴏʙɪᴛᴀ ᴘᴀᴘᴀ • **"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("•ᴀᴅᴅ ᴍᴇ•", url=f"https://t.me/NOBITA_MUSIC_ROBOT?startgroup=true")
        ],
        [
          InlineKeyboardButton("•sᴜᴘᴘᴏʀᴛ•", url="https://t.me/+ClpXmI00B7UxYjc1"),
          InlineKeyboardButton("•ᴏᴡɴᴇʀ•", url="https://t.me/ll_NOBITA_DEFAULTERS_ll"),
          ],
               [
                InlineKeyboardButton("•ᴜᴘᴅᴀᴛᴇs•", url="https://t.me/NOB1TA_SUPPORT"),

],
[
              InlineKeyboardButton("˹ɴᴏʙɪᴛᴀ ꭙ ᴍᴜꜱɪᴄ˼ ♪", url=f"https://t.me/NOBITA_MUSIC_ROBOT"),
              InlineKeyboardButton("︎˹ɴᴏʙɪᴛᴀ ꭙ ᴍᴜꜱɪᴄ˼ 2 ♪", url=f"https://t.me/NOBITA_MUSIC_TG_BOT"),
              ],
              [
              InlineKeyboardButton("˹ 𝐕ᴀɴsʜɪᴋᴀ ꭙ 𝐌ᴜsɪᴄ ˼ ♪ [ ", url=f"https://t.me/VanshikaMusicRobot"),
InlineKeyboardButton("˹ ᰻⃪᱂𝛂፝֟𝛎𝛂ꪀ ꭙ 𐌼⃪𝛖𝛅𝛊ᴄ ˼", url=f"https://t.me/RavanMusicBot"),
],
[
InlineKeyboardButton("˹ 𝐄ʟɪᴛᴇ ꭙ 𝐌ᴜsɪᴄ ˼", url=f"https://t.me/EliteMusicRobot"),
InlineKeyboardButton("˹ 𝐍ᴏʙɪᴛᴀ ꭙ 𝐂ᴀᴛᴄʜᴇʀ ˼", url=f"https://t.me/NobitaGrabberBot"),
],
[
              InlineKeyboardButton("•ᴅᴇғᴀᴜʟᴛᴇʀs ɢᴄ•", url=f"https://t.me/+ClpXmI00B7UxYjc1"),
              InlineKeyboardButton("˹ɴᴏʙɪᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ˼", url=f"https://t.me/NOB1TA_SUPPORT"),
              ],
              [
              InlineKeyboardButton("ᴀʟʟ ʙᴏᴛ", url=f"https://t.me/NOB1TA_SUPPORT/10"),
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/tcz7s6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/BABY-MUSIC/BABYTUNE/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[•ʙᴏᴛ-ᴏᴡɴᴇʀ•](https://t.me/ll_NOBITA_DEFAULTERS_ll) | [•ᴜᴘᴅᴀᴛᴇs•](https://t.me/NOB1TA_SUPPORT)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
