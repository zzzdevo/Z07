import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID, SUPPORT_CHANNEL, OWNER_CHANNEL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from DAXXMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from DAXXMUSIC import app
from random import  choice, randint

                
@app.on_message(
    command(["/source", "سەرچاوە", "سۆرس", "گەشەپێدەران"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/b4ace5c5aec2901efed59.jpg",
        caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 گەشەپێدەران](t.me/MGIMT)**\n••┉┉┉┉┉••🝢••┉┉┉┉┉••\n**بەخێربێی ئەزیزم{message.from_user.mention} بۆ بەشی گەشەپێدەرانی بۆت🕷️•**\n**بۆ هەبوونی هەرکێشە و پرسیارێك پەیوەندی بە گەشەپێدەر بکە لەڕێگای دووگمەکانی خوارەوە♥•**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ محمد ✬", url=f"https://t.me/IQ7amo"), 
                 ],[
                    
                
                    InlineKeyboardButton(
                        "𐇮 ﮼ﺣ‌ّــەمــە 🇧🇷 𐇮", url=f"https://t.me/VTVIT"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"https://t.me/MGIMT"),
                
        ],[
                    
                
                    InlineKeyboardButton(
                        "『𓏺کەناڵی سەرەکی』", url=f"https://t.me/xv7amo"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["حەمە", "@VTVIT", "گەشەپێدەر"])
 
)
async def yas(client, message):
    
    usr = await client.get_chat("VTVIT")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - سەرچاوەی زیرەك 🧑🏻‍💻](t.me/MGIMT)\nزانیاری گەشەپێدەری دووەمی بۆت\n↜︙𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙𝐈𝐃 ↬ :`{usr.id}`\n↜︙𝐁𝐈𝐎 ↬: {usr.bio}**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
   command(["پڕۆگرامساز"])
   
)
async def yas(client, message):
    usr = await client.get_chat("IQ7amo")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 پڕۆگرامساز](t.me/MGIMT)\nزانیاری پڕۆگرامسازی سەرچاوە\n↜︙𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙𝐈𝐃 ↬ :`{usr.id}`\n↜︙𝐁𝐈𝐎 ↬: {usr.bio}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],  [
                    InlineKeyboardButton(
                        "🝢 پەیوەندی کردن 🝢", url=f"https://t.me/{usr.username}"),                        
                 ],
            ]
        ),
    )


@app.on_message(
  command(["سەرۆک", "@IQ7amo"])
  
)
async def yas(client, message):
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 خاوەنی بۆت](t.me/MGIMT)\nزانیاری خاوەنی بۆت\n↜︙𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙𝐈𝐃 ↬ :`{usr.id}`\n↜︙𝐁𝐈𝐎 ↬: {usr.bio}**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],   [
                    InlineKeyboardButton(
                        "🝢 پەیوەندی کردن 🝢", url=f"https://t.me/{usr.username}"),                        
                 ],
                      [
                    InlineKeyboardButton(
                        "کەناڵی گەشەپێدەر", url=f"https://t.me/MGIMT"),                        
                 ],
            ]
        ),
    )
@app.on_message(
   command(["کەناڵ", "کەنال"])
   
)
async def yas(client, message):
    usr = await client.get_chat(OWNER_CHANNEL)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - کەناڵی سەرچاوە 🧑🏻‍💻](t.me/MGIMT)**\n**جۆینی کەناڵی بۆت بکە بۆ بینینی بابەتی جیاوازتر♥**\n\n** بەستەری کەناڵ :\nhttps://t.me/{usr.username}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌 - سەرچاوەی زیرەك", url=f"https://t.me/{usr.username}")
                ], 
            ]
        ),
    )



@app.on_message(
   command(["زیرەکی دەستکرد"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7713aee1676f475d4ed21.jpg",
        caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - زیرەکی دەستکرد🧑🏻‍💻🖤](t.me/MGIMT)**\n\n**بەخێربێی ئەزیزم {message.from_user.mention} بۆ بەشی زیرەکی دەستکرد تایبەت بە سەرچاوەی زیرەك**\n** بۆ بەکارهێنانی بنووسە : iq + پرسیارەکەت ♥⚡**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                                        InlineKeyboardButton(
                        "﮼محمد˹َّّ", url=f"https://t.me/IQ7amo"), 
                 ],[
                
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"https://t.me/MGIMT"),
                ],

            ]

        ),

    )



@app.on_message(
   command(["قورئان"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/78cefd067cff33d79edb7.jpg",
        caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - پەخشی قورئان🧑🏻‍💻🖤](t.me/MGIMT)**\n\n**بەخێربێی ئەزیزم {message.from_user.mention} بۆ بەشی پەخشکردنی قورئانی پیرۆز تایبەت بە سەرچاوەی زیرەك**\n** بۆ پەخشکردنی بنووسە : سوڕەتی یان سوڕەت + ناوی سوڕەت ♥⚡**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "﮼محمد˹َّّ", url=f"https://t.me/IQ7amo"), 
                 ],[
                
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"https://t.me/MGIMT"),
                 ],

            ]

        ),

    )

    
