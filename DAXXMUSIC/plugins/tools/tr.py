from pyrogram import filters
from pyrogram.types import *
from DAXXMUSIC import app
from gpytranslate import Translator
from strings.filters import command

#.......

trans = Translator()

#......

@app.on_message(command(["/tr","وەرگێران","وەرگێڕان"]))
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("**➠ | وەڵامی نامەکە بدەوە کە دەتەوێ وەرگێڕانی بۆ بکەم\nبەکارهێنان:\n/tr en ڕیپلەی نامەیە بکە وەریدەگێڕێتە سەر زمانی ئینگلیزی**")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"**وەرگێڕدرا لە {source} بۆ {dest}:\n\n**"
        f"**{translation.text}**"
    )
    await message.reply_text(reply)
