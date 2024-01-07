from telebot.async_telebot import AsyncTeleBot
from telebot.types import  Message
from telemod import Listener
import asyncio, json, os

# @BENN_DEV & @BENfiles
token = "BOT TOKEN" # YOUR BOT TOEKN
app = AsyncTeleBot(token, parse_mode="Markdown")
loop = asyncio.get_event_loop()
listener = Listener(app, loop)
owner = 5451878368 # YOUR ID


@app.message_handler(commands=["start"], func= lambda message: message.from_user.id != owner)
async def start(message: Message):
    user_id = message.from_user.id
    if user_id in banned: return await app.reply_to(message, "- أنت محظور من استخدام البوت.")
    info = await app.get_chat(owner)
    name = info.first_name
    username = info.username
    url = f"{username}.t.me"
    await app.reply_to(
        message,
        f"- مرحبًا عزيزي في بوت تواصل [{name}]({url}).\nقم بإرسال ما تريد وسيتم تحويل رسالتك للمالك."
    )
    
     
@app.message_handler(commands=["start"], func= lambda message: message.from_user.id == owner)
async def admin(message: Message):
    await app.reply_to(
        message,
        "- مرحبًا عزيزي المالك.\n- يقوم البوت بإستلام الرسائل من المستخدمين وتوجيهها اليك.\n- اذا كنت تريد (الغاء) حظر شخص ما استخدم (الغاء) حظر + الايدي."
    )
    

@app.message_handler(
    content_types=["text", "audio", "video", "photo", "document", "dice", "video_note", "voice"],
    func = lambda message: message.from_user.id == owner and message.reply_to_message)
async def reply(message: Message):
    try: user_id = message.reply_to_message.forward_from.id
    except AttributeError: return await app.reply_to(message, "قم هذا المستخدم بإخفاء معلوماته!")
    await app.copy_message(
        chat_id=user_id, 
        from_chat_id=owner,
        message_id=message.id
    )
    await app.reply_to(message,"- تم الرد.")


@app.message_handler(regexp=r"^(حظر|الغاء حظر)")
async def ban(message: Message):
    data = message.text.rsplit(" ", 1)
    if len(data) != 2: return await app.reply_to(message, "- بيانات غير صحيحه.")
    try: user_id = int(data[1])
    except TypeError: return await app.reply_to(message, "- بيانات غير صحيحه.")
    if data[0] == "حظر":
        if user_id in banned: return await app.reply_to(message, "- هذا المستخدم محظور بالفعل.")
        banned.append(user_id)
    else:
        if user_id not in banned: return await app.reply_to(message, "- هذا المستخدم غير محظور.")
        banned.remove(user_id)
    write(banned_db, banned)
    await app.reply_to(message, f"تم {data[0]} هذا المستخدم. ")


@app.message_handler(
    content_types=["text", "audio", "video", "photo", "document", "dice", "video_note", "voice"],
    func = lambda message: message.from_user.id != owner)
async def router(message: Message):
    user_id = message.from_user.id
    if user_id in banned: return await app.reply_to(message,"- أنت محظور من استخدام البوت.")
    await app.forward_message(
        from_chat_id=user_id,
        chat_id=owner,
        message_id=message.id
    )
    await app.reply_to(message,"تم ارسال رسالتك للمالك.")


def write(fp, data):
    with open(fp, "w") as f:
        json.dump(data, f, indent=2)


def read(fp):
    if not os.path.exists(fp): write(fp, [])
    with open(fp) as f:
        data = json.load(f)
    return data
 

banned_db = "banned.json"
banned = read(banned_db)


async def main():
    print((await app.get_me()).full_name)
    await app.infinity_polling()


if __name__ == "__main__": loop.run_until_complete(main())
# 𝗪𝗥𝗜𝗧𝗧𝗘𝗡 𝗕𝗬 : @BENN_DEV
# 𝗦𝗢𝗨𝗥𝗖𝗘 : @BENfiles