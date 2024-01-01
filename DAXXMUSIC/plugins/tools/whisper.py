from DAXXMUSIC import app as app
from config import BOT_USERNAME
from pyrogram import filters
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton
)

whisper_db = {}

switch_btn = InlineKeyboardMarkup([[InlineKeyboardButton("⚡ دەستپێکردنی چرپەنامە ⚡", switch_inline_query_current_chat="")]])

async def _whisper(_, inline_query):
    data = inline_query.query
    results = []
    
    if len(data.split()) < 2:
        mm = [
            InlineQueryResultArticle(
                title="⚡ چرپەنامە ⚡",
                description=f"@{BOT_USERNAME} [ یوزەر | ئایدی ] [ نووسین ]",
                input_message_content=InputTextMessageContent(f"**💒 بەکارهێنان**:\n\n@{BOT_USERNAME} [ یوزەر | ئایدی ] [ نووسین ]"),
                thumb_url="https://te.legra.ph/file/3eec679156a393c6a1053.jpg",
                reply_markup=switch_btn
            )
        ]
    else:
        try:
            user_id = data.split()[0]
            msg = data.split(None, 1)[1]
        except IndexError as e:
            pass
        
        try:
            user = await _.get_users(user_id)
        except:
            mm = [
                InlineQueryResultArticle(
                    title="⚡ چرپەنامە ⚡",
                    description="**یوزەر یان ئایدی هەڵەیە!**",
                    input_message_content=InputTextMessageContent("**یوزەر یان ئایدی هەڵەیە!**"),
                    thumb_url="https://te.legra.ph/file/3eec679156a393c6a1053.jpg",
                    reply_markup=switch_btn
                )
            ]
        
        try:
            whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("⚡ چرپەنامە ⚡", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}")]])
            one_time_whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("🔩 چرپەنامەی یەکجاری", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}_one")]])
            mm = [
                InlineQueryResultArticle(
                    title="⚡ چرپەنامە ⚡",
                    description=f"چرپەنامەیەكت نارد بۆ {user.first_name}!",
                    input_message_content=InputTextMessageContent(f"**⚡ تۆ چرپەیەکت نارد بۆ {user.first_name}.\n\nتەنیا ئەو دەتوانێت بیکاتۆ**"),
                    thumb_url="https://te.legra.ph/file/3eec679156a393c6a1053.jpg",
                    reply_markup=whisper_btn
                ),
                InlineQueryResultArticle(
                    title="🔩 One-Time Whisper",
                    description=f"Send a one-time whisper to {user.first_name}!",
                    input_message_content=InputTextMessageContent(f"**🔩 تۆ چرپەیەکی یەکجارەکی دەنێری بۆ {user.first_name}.\n\nتەنیا ئەو دەتوانێت بیکاتۆ**"),
                    thumb_url="https://te.legra.ph/file/3eec679156a393c6a1053.jpg",
                    reply_markup=one_time_whisper_btn
                )
            ]
        except:
            pass
        
        try:
            whisper_db[f"{inline_query.from_user.id}_{user.id}"] = msg
        except:
            pass
    
    results.append(mm)
    return results


@app.on_callback_query(filters.regex(pattern=r"fdaywhisper_(.*)"))
async def whispes_cb(_, query):
    data = query.data.split("_")
    from_user = int(data[1])
    to_user = int(data[2])
    user_id = query.from_user.id
    
    if user_id not in [from_user, to_user, 833360381]:
        try:
            await _.send_message(from_user, f"{query.from_user.mention} هەوڵدەدات چرپەی تۆ بکاتەوە")
        except Unauthorized:
            pass
        
        return await query.answer("ئەم چرپەیە بۆتۆ نییە 🚧", show_alert=True)
    
    search_msg = f"{from_user}_{to_user}"
    
    try:
        msg = whisper_db[search_msg]
    except:
        msg = "**🚫 هەڵە !\n\nچرپەنامە سڕدرایەوە لە داتابەیس**"
    
    SWITCH = InlineKeyboardMarkup([[InlineKeyboardButton("بڕۆ بۆ دووگمە 🪝", switch_inline_query_current_chat="")]])
    
    await query.answer(msg, show_alert=True)
    
    if len(data) > 3 and data[3] == "one":
        if user_id == to_user:
            await query.edit_message_text("**📬 چرپە خوێندرایەوە!\n\nبۆ ناردنی چرپە دوگمەی خوارەوە داگرە!**", reply_markup=SWITCH)


async def in_help():
    answers = [
        InlineQueryResultArticle(
            title="⚡ چرپەنامە ⚡",
            description=f"@IQMCBOT [یوزەر | ئایدی] [ نووسین ]",
            input_message_content=InputTextMessageContent(f"**📍بەکارهێنان:**\n\n@IQMCBOT (یوزەر یان ئایدی کەسەکە) (نامەکەت).\n\n**نموونە:**\n@IQMCBOT @IQ7amo سەرۆک"),
            thumb_url="https://te.legra.ph/file/3eec679156a393c6a1053.jpg",
            reply_markup=switch_btn
        )
    ]
    return answers


@app.on_inline_query()
async def bot_inline(_, inline_query):
    string = inline_query.query.lower()
    
    if string.strip() == "":
        answers = await in_help()
        await inline_query.answer(answers)
    else:
        answers = await _whisper(_, inline_query)
        await inline_query.answer(answers[-1], cache_time=0)
                                               
