import random 
from pyrogram import filters,Client,enums
from DAXXMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions
from strings.filters import command
from DAXXMUSIC.mongo.nightmodedb import nightdb,nightmode_on,nightmode_off,get_nightchats 



CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages = False,
    can_send_other_messages = False,
    can_send_polls = False,
    can_change_info = False,
    can_add_web_page_previews = False,
    can_pin_messages = False,
    can_invite_users = False )


OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages = True,
    can_send_other_messages = True,
    can_send_polls = True,
    can_change_info = True,
    can_add_web_page_previews = True,
    can_pin_messages = True,
    can_invite_users = True )
    
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("๏ چالاککردن ๏", callback_data="add_night"),InlineKeyboardButton("๏ ناچالاککردن ๏", callback_data="rm_night")]])         

@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg", caption="**๏ کلیك بکە لە یەکێك لە دوگمەکان بۆ چالاککردن و ناچالاککردنی دۆخی شەو\nفەرمانەکە بۆ داخستن و کردنەوەی گرووپە بۆ خودکار🖤•**",reply_markup=buttons)
              
     
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query : CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id" : chat_id})
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
    if user_id in administrators:   
        if data == "add_night":
            if check_night:        
                await query.message.edit_caption("**๏ دۆخی شەو پێشتر چالاککراوە!**")
            elif not check_night :
                await nightmode_on(chat_id)
                await query.message.edit_caption("**๏ دۆخی شەو لەم گرووپە زیادکرا بۆ داتا بیسم، گرووپ کاتژمێر 𝟏𝟐ی شەو دادەخرێت وە کاتژمێر 𝟖ی بەیانی دەکرێتەوە**") 
        if data == "rm_night":
            if check_night:  
                await nightmode_off(chat_id)      
                await query.message.edit_caption("**๏ زانیاری دۆخی شەو سڕدرایەوە لە داتا بەیسم**")
            elif not check_night:
                await query.message.edit_caption("**๏ دۆخی شەو پێشتر ناچالاککراوە!**") 
            
    
    
async def start_nightmode() :
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await app.send_video(
                add_chat,
                video="https://telegra.ph/file/76986c01e5b54f7b7c503.mp4",
                caption= f"**گرووپ دادەخرێت ئەزیزان🚫🧑🏻‍💻\nبەهیوای خەوێکی خۆش و ئارام خودای گەورە بەختەوەرتان بکات شەوتان شاد🌚♥️🫶🏻**")
            
            await app.set_chat_permissions(add_chat,CLOSE_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To close Group {add_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Baghdad")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.start()

async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://graph.org/file/765ad5ac25fca83c1d06c.jpg",
                caption= f"**گرووپ کرایەوە ئەزیزان✅🧑🏻‍💻\nبەیانیتان باش🌚♥️🫶🏻**")
            
            await app.set_chat_permissions(rm_chat,OPEN_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To open Group {rm_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Baghdad")
scheduler.add_job(close_nightmode, trigger="cron", hour=8, minute=1)
scheduler.start()

##############################

@app.on_message(command("دۆخی شەو") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg", caption="**๏ کلیك بکە لە یەکێك لە دوگمەکان بۆ چالاککردن و ناچالاککردنی دۆخی شەو\nفەرمانەکە بۆ داخستن و کردنەوەی گرووپە بۆ خودکار🖤•**",reply_markup=buttons)

