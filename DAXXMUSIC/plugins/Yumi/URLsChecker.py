from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button
import pyrogram.errors, requests, re


app = Client(
    "URLsChecker",
    api_id = 1384,
    api_hash = "99172839e8a8d95052",
    bot_token = "6553005927:AAH2CTrI"
)


@app.on_message(filters.command("start"))
async def start(_, message: Message):
    user_id = message.from_user.id
    subscribe = await subscription(user_id)
    if subscribe: return await message.reply_text(
        f"- Sorry You Need To Subscribe To Our Channel First.\n- channel: {subscribe['channel']}\n- Subscribe Then send: /start",
        reply_to_message_id = message.id)
    name = (await app.get_chat(5451878368)).first_name
    caption = "- Welcome To URLs Checker Bot.\n- Send Me A Link To Chek It."
    markup = Keyboard([
        [Button(name, url="BENN_DEV.t.me")]
    ])
    await message.reply_text(
        caption,
        reply_markup=markup,
        reply_to_message_id=message.id
    )
        

@app.on_message(filters.regex(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"))
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
        if positives == 0: return await message.reply_text("- Safe Url ✅️", reply_to_message_id=message.id)
        caption = "- Unsafe URL ⚠️\n- Reasons: \n"
        try:
            for scan in scan_result.get("scans").values():
                if scan.get("detected"): caption += f"- {scan.get('name')}\n"
        except: ...
        return await message.reply_text(
            caption,
            reply_to_message_id=message.id
        )
    await message.reply_text(
        "- There is NO Response.\n- Try Again, Please.",
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
    channel = "@BENfiles"
    try: await app.get_chat_member(chat_id=channel, user_id=user_id)
    except pyrogram.errors.exceptions.bad_request_400.UserNotParticipant: return {"channel" : channel}
    return False


def main():
    print("Alive")
    app.run()
    

if __name__ == "__main__": main()