from pyrogram import Client, filters
from pyrogram.types import Message
from DAXXMUSIC import app
from pyrogram.types import InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button
import pyrogram.errors, requests, re


markup2 = markup = Keyboard([
        [Button("”﮼احساس“ !", url="https://t.me/xv7amo")]
    ])

@app.on_message(filters.command(["chk","پشکنین","پشکنين"], prefixes=["/", "", "#"]))
async def start(_, message: Message):
    user_id = message.from_user.id
    subscribe = await subscription(user_id)
    if subscribe: return await message.reply_text(
        f"**🧑🏻‍💻︙ببوورە ئەزیزم تۆ جۆین نیت؛\n🔰︙سەرەتا پێویستە جۆینی کەناڵی بۆت ♥️؛\n👾︙بکەیت بۆ بەکارهێنانم جۆین بە ⚜️؛\n💎︙کەناڵی بۆت: {subscribe['channel']}\n\n👾︙کاتێ جۆینت کرد پشکنین بکە /chk , پشکنین 📛!**",
        reply_markup=markup2,
        reply_to_message_id = message.id)
    name = (await app.get_chat(6357186923)).first_name
    caption = "**👾︙بەخێربێی بۆ فەرمانی پشکنین بۆ لینکی ساختە\n👾︙لینک لە تایبەتی بۆت بنێرە**"
    markup = Keyboard([
        [Button(name, url="https://t.me/IQMCBOT")]
    ])
    await message.reply_text(
        caption,
        reply_markup=markup,
        reply_to_message_id=message.id
    )
        

@app.on_message(filters.regex(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)") & filters.private)
async def responseer(_, message: Message):
    pattern = re.compile(
        r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"
    )
    URLs = re.findall(pattern, message.text)
    for url in URLs:
        await checker(message, url)


async def checker(message: Message, url):
    try: scan_response = scan_url(url)
    except: return await message.reply_text("- Invalid URL", reply_to_message_id=message.id)
    scan_id = scan_response.get("scan_id")
    if scan_id:
        scan_result = get_scan_result(scan_id)
        positives = scan_result.get("positives")
        if positives == 0: return await message.reply_text("**• لینک پارێزراوە پاکە ✅️**", reply_to_message_id=message.id)
        caption = "**• لینک پارێزراو نییە ⚠️\n• هۆکار: \n**"
        try:
            for scan in scan_result.get("scans").values():
                if scan.get("detected"): caption += f"- {scan.get('name')}\n"
        except: ...
        return await message.reply_text(
            caption,
            reply_to_message_id=message.id
        )
    await message.reply_text(
        "**• هیچ وەڵامدانەوەیە نەبوو\n• تکایە دووبارەی بکەوە♻️🖤**",
        reply_to_message_id=message.id
    )


api_key = "25b21ebb13c3b02ed2790c30d09d127b5a4e61b76b07026f54642bc740c77559"
def scan_url(url):
    params = {
        "apikey": api_key,
        "url": url 
    }
    url = "https://www.virustotal.com/vtapi/v2/url/scan"
    response = requests.post(url, params=params)
    json_response = response.json()
    return json_response


def get_scan_result(resource):
    params = {
        "apikey": api_key,
        "resource": resource
    }
    url = "https://www.virustotal.com/vtapi/v2/url/report"
    response = requests.get(url, params=params)
    json_response = response.json()
    return json_response

async def subscription(user_id):
    channel = "@xv7amo"
    try: await app.get_chat_member(chat_id=channel, user_id=user_id)
    except pyrogram.errors.exceptions.bad_request_400.UserNotParticipant: return {"channel" : channel}
    return False
