from asyncio import sleep
from pyrogram import filters
from pyrogram.enums import ChatType
from DAXXMUSIC.misc import SUDOERS
from pyrogram.errors import MessageDeleteForbidden, RPCError
from pyrogram.types import Message
from DAXXMUSIC.utils.daxx_ban import admin_filter
from DAXXMUSIC import app


@app.on_message(filters.command("purge") & admin_filter & SUDOERS)
async def purge(app: app, msg: Message):
    
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**ناتوانم نامەکان پاکبکەمەوە لە گرووپێکی بنەڕەتیدا گرووپێکی گشتی دروست بکە🖤•**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        
        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
                
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**من ناتوانم هەموو نامەکان بسڕمەوە، لەوانەیە نامەکان کۆن بن یان لەوانەیە مافی یان ڕۆڵی سڕینەوەم نەبێ یان گرووپێکی گشتی نەبێ‌🖤•**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**هەندێك هەڵە هەیە, ڕیپۆرتی بکە بەبەکارهێنانی** `/bug`<b>هەڵە:</b> <code>{ef}</code>")
        count_del_msg = len(message_ids)
        sumit = await msg.reply_text(text=f"**سڕدرایەوە <i>{count_del_msg}</i> نامە**")
        await sleep(3)
        await sumit.delete()
        return
    await msg.reply_text("**وەڵامی نامەیەك بدەوە بۆ دەستپێکردنی پاککردنەوە**")
    return





@app.on_message(filters.command("spurge") & admin_filter & SUDOERS)
async def spurge(app: app, msg: Message):

    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**ناتوانم نامەکان پاکبکەمەوە لە گرووپێکی بنەڕەتیدا گرووپێکی گشتی دروست بکە🖤•**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**من ناتوانم هەموو نامەکان بسڕمەوە، لەوانەیە نامەکان کۆن بن یان لەوانەیە مافی یان ڕۆڵی سڕینەوەم نەبێ یان گرووپێکی گشتی نەبێ‌🖤•**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**هەندێك هەڵە هەیە, ڕیپۆرتی بکە بەبەکارهێنانی** `/bug`<b>هەڵە:</b> <code>{ef}</code>")           
            return        
    await msg.reply_text("**وەڵامی نامەیەك بدەوە بۆ دەستپێکردنی پاککردنەوە**")
    return


@app.on_message(filters.command("del") & admin_filter & SUDOERS)
async def del_msg(app: app, msg: Message):
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**ناتوانم نامەکان پاکبکەمەوە لە گرووپێکی بنەڕەتیدا گرووپێکی گشتی دروست بکە🖤•**")
        return        
    if msg.reply_to_message:
        await msg.delete()
        await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.reply_to_message.id)
    else:
        await msg.reply_text(text="**چی شتێکت دەوێت بۆ سڕینەوە🖤؟**")
        return


