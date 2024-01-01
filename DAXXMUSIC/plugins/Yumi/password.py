import random, os
from pyrogram import Client, filters, enums 
from strings.filters import command
from DAXXMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(command(["genpassword", "genpw","پاسوۆرد","پاسورد"]))
async def password(bot, update):
    message = await update.reply_text(text="** پڕۆسەی دەکات..**")
    password = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+".lower()
    if len(update.command) > 1:
        qw = update.text.split(" ", 1)[1]
    else:
        ST = ["5", "7", "6", "9", "10", "12", "14", "8", "13"] 
        qw = random.choice(ST)
    limit = int(qw)
    random_value = "".join(random.sample(password, limit))
    txt = f"<b>سنووردار:</b> {str(limit)} \n<b>پاسوۆرد: </b><code>{random_value}</code>"
    btn = InlineKeyboardMarkup([[InlineKeyboardButton('𝗔𝗗𝗗 𝗠𝗘', url='https://t.me/IQMCBOT?startgroup=true')]])
    await message.edit_text(text=txt, reply_markup=btn, parse_mode=enums.ParseMode.HTML)
