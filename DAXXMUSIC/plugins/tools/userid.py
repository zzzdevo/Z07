from DAXXMUSIC import app
from pyrogram import filters
from pyrogram.enums import ParseMode
from strings.filters import command


@app.on_message(command(["me", "/me",]))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ئایدیەکەت**: `{message.from_user.id}`\n{reply.from_user.first_name}' ئایدی: {reply.from_user.id}\n**ئایدی گرووپ**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ئایدیەکەت:** `{message.from_user.id}`\n**ئایدی گرووپ:** `{message.chat.id}`"
        )

####

@app.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ئایدی نامە:]({message.link})** `{message_id}`\n"
    text += f"**[ئایدییەکەت:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ئایدی بەکارهێنەر:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("بەکارهێنەر نییە", quote=True)

    text += f"**[ئایدی گرووپ:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ئایدی نامەی کەسی بەرامبەر:]({reply.link})** `{reply.id}`\n"
        text += f"**[ئایدی کەسی بەرامبەر:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"**کەناڵی فۆروارد کراو, {reply.forward_from_chat.title}, \nوە ئایدییەکەی: `{reply.forward_from_chat.id}` **\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"** ئایدی گرووپ یان کەناڵی ڕپلەی کراو:** `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )
