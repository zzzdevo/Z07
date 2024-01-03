import re
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.daxx_ban import admin_filter
from DAXXMUSIC.mongo.filtersdb import *
from DAXXMUSIC.utils.filters_func import GetFIlterMessage, get_text_reason, SendFilterMessage
from DAXXMUSIC.utils.yumidb import user_admin
from pyrogram import filters
from DAXXMUSIC.misc import SUDOERS
from strings.filters import command
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


@app.on_message(command("زیادکردنی چات") & admin_filter & SUDOERS)
@user_admin
async def _filter(client, message):
    
    chat_id = message.chat.id 
    if (
        message.reply_to_message
        and not len(message.command) == 2
    ):
        await message.reply("**پێویستە ناوێکم پێبدەیت🖤•**")  
        return 
    
    filter_name, filter_reason = get_text_reason(message)
    if (
        message.reply_to_message
        and not len(message.command) >=2
    ):
        await message.reply("پێویستە هەندێک ناوەڕۆک بدەیت بە چاتەکە🖤•**")
        return

    content, text, data_type = await GetFIlterMessage(message)
    await add_filter_db(chat_id, filter_name=filter_name, content=content, text=text, data_type=data_type)
    await message.reply(
        f"**چات زیادکرا بە ناوی ↤︎ `{filter_name}` ♥•**"
    )


@app.on_message(~filters.bot & filters.group, group=4)
async def FilterCheckker(client, message):
    if not message.text:
        return
    text = message.text
    chat_id = message.chat.id
    if (
        len(await get_filters_list(chat_id)) == 0
    ):
        return

    ALL_FILTERS = await get_filters_list(chat_id)
    for filter_ in ALL_FILTERS:
        
        if (
            message.command
            and message.command[0] == 'filter'
            and len(message.command) >= 2
            and message.command[1] ==  filter_
        ):
            return
            
        pattern = r"( |^|[^\w])" + re.escape(filter_) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            filter_name, content, text, data_type = await get_filter(chat_id, filter_)
            await SendFilterMessage(
                message=message,
                filter_name=filter_,
                content=content,
                text=text,
                data_type=data_type
            )

@app.on_message(command("چاتەکان") & filters.group)
async def _filters(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title 
    if message.chat.type == 'private':
        chat_title = 'local'
    FILTERS = await get_filters_list(chat_id)
    
    if len(FILTERS) == 0:
        await message.reply(
            f'**هیچ چاتێکی زیادکراو نییە لە {chat_title} ♥•**'
        )
        return

    filters_list = f'**لیستی چاتە زیادکراوەکانی {chat_title}:\n♥•**'
    
    for filter_ in FILTERS:
        filters_list += f'**❍ `{filter_}`\n**'
    
    await message.reply(
        filters_list
    )


@app.on_message(command(["سڕینەوەی چاتەکان","سرینەوەی چاتەکان"]) & admin_filter & SUDOERS)
async def stopall(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title 
    user = await client.get_chat_member(chat_id,message.from_user.id)
    if not user.status == ChatMemberStatus.OWNER :
        return await message.reply_text("**تەنیا سەرۆك گرووپ دەتوانێت♥•**") 

    KEYBOARD = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='سڕینەوەی هەموو چاتەکان', callback_data='custfilters_stopall')],
        [InlineKeyboardButton(text='هەڵوەشانەوە', callback_data='custfilters_cancel')]]
    )

    await message.reply(
        text=(f'**ئایا دڵنیای کە دەتەوێت هەموو چاتە زیادکراوەکان لە ئەم کردارەدا بوەستێنیت؟♥•**'),
        reply_markup=KEYBOARD
    )


@app.on_callback_query(filters.regex("^custfilters_"))
async def stopall_callback(client, callback_query: CallbackQuery):  
    chat_id = callback_query.message.chat.id 
    query_data = callback_query.data.split('_')[1]  

    user = await client.get_chat_member(chat_id, callback_query.from_user.id)

    if not user.status == ChatMemberStatus.OWNER :
        return await callback_query.answer("تەنیا سەرۆك گرووپ دەتوانێت") 
    
    if query_data == 'stopall':
        await stop_all_db(chat_id)
        await callback_query.edit_message_text(text="بە سەرکەوتوویی هەموو چاتەکان سڕدرانەوە♥️✅")
    
    elif query_data == 'cancel':
        await callback_query.edit_message_text(text='بە سەرکەوتوویی هەڵوەشێنرایەوە♥️✅')



@app.on_message(command(["سرینەوەی چات","سڕینەوەی چات"]) & admin_filter & SUDOERS)
@user_admin
async def stop(client, message):
    chat_id = message.chat.id
    if not (len(message.command) >= 2):
        await message.reply('Use Help To Know The Command Usage')
        return
    
    filter_name = message.command[1]
    if (filter_name not in await get_filters_list(chat_id)):
        await message.reply("**هیچ چاتێكت زیاد نەکردووە ئەزیزم👾**")
        return
    
    await stop_db(chat_id, filter_name)
    await message.reply(f"**بە سەرکەوتوویی چاتە زیادکراوەکە سڕایەوە: `{filter_name}`♥•**")
