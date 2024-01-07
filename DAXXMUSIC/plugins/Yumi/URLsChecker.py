from pyrogram import Client, filters
from pyrogram.types import Message
from DAXXMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import pyrogram.errors, requests, re



@app.on_message(filters.command(["chk","پشکنین","پشکنين"], prefixes=["/", "", "#"]))
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/024f02f6681c3785ec085.jpg",
        caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - فەرمانی پشکنین🧑🏻‍💻🖤](t.me/MGIMT)**\n\n**بەخێربێی ئەزیزم {message.from_user.mention} بۆ بەشی پشکنینی لینك تایبەت بە سەرچاوەی زیرەك**\n** بۆ بەکارهێنانی: بڕۆ چاتی بۆت @IQMCBOT و لینك دابنێ بۆتی دەپشکنێ پێت دەڵێت پارێزراوە یان نا♥⚡**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                                        InlineKeyboardButton(
                        "𝙄𝙌 𝙈𝙐𝙎𝙄𝘾 ♥️•", url=f"https://t.me/IQMCBOT"), 
                 ],[
                
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"https://t.me/MGIMT"),
                ],

            ]

        ),

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
    except: return await message.reply_text("**• لینکی هەڵە**", reply_to_message_id=message.id)
    scan_id = scan_response.get("scan_id")
    if scan_id:
        scan_result = get_scan_result(scan_id)
        positives = scan_result.get("positives")
        if positives == 0: return await message.reply_text("**• لینک پارێزراوە پاکە ✅️**", reply_to_message_id=message.id)
        caption = "**• لینک پارێزراو نییە ⚠️\n• هۆکار: \n**"
        try:
            for scan in scan_result.get("scans").values():
                if scan.get("detected"): caption += f"• {scan.get('name')}\n"
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

        
