from pyrogram import filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)

import datetime
from DAXXMUSIC import app




def mention(user, name, mention=True):
    if mention == True:
        link = f"[{name}](tg://openmessage?user_id={user})"
    else:
        link = f"[{name}](https://t.me/{user})"
    return link



async def get_userid_from_username(username):
    try:
        user = await app.get_users(username)
    except:
        return None
    
    user_obj = [user.id, user.first_name]
    return user_obj


async def ban_user(user_id, first_name, admin_id, admin_name, chat_id, reason, time=None):
    try:
        await app.ban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        msg_text = "**ڕۆڵی دەرکردنم نییە، ڕۆڵی باندم پێبدە بۆ ئەنجامدانی💘•**"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "**من ناتوانم ئەدمین دەربکەم بەجدیتە؟😂🙂**"
        return msg_text, False
    except Exception as e:
        if user_id == 833360381:
            msg_text = "**بۆچی دەتەوێ خۆم دەربکەم؟ نا ببورە من وەکو تۆ گەمژەنیم😂🙂!**"
            return msg_text, False
        
        msg_text = f"**ئۆپسس😂🙂\n{e}**"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)

    msg_text += f"**دەرکرا: {user_mention}\nلەلایەن: {admin_mention}**"
    
    if reason:
        msg_text += f"**هۆکار: `{reason}`\n**"
    if time:
        msg_text += f"**کات: `{time}`\n**"

    return msg_text, True


async def unban_user(user_id, first_name, admin_id, admin_name, chat_id):
    try:
        await app.unban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        msg_text = "**ڕۆڵی لادانی دەرکردنم نییە، ڕۆڵی باندم پێبدە بۆ ئەنجامدانی💘•**"
        return msg_text
    except Exception as e:
        msg_text = f"**ئۆپسس😂🙂\n{e}**"
        return msg_text

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    
    msg_text = f"**دەرکردنی لەسەر لادرا: {user_mention}\nلەلایەن: {admin_mention}**"
    return msg_text



async def mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason, time=None):
    try:
        if time:
            mute_end_time = datetime.datetime.now() + time
            await app.restrict_chat_member(chat_id, user_id, ChatPermissions(), mute_end_time)
        else:
            await app.restrict_chat_member(chat_id, user_id, ChatPermissions())
    except ChatAdminRequired:
        msg_text = "**ڕۆڵی میوتکردنم نییە، ڕۆڵی میوتم پێبدە بۆ ئەنجامدانی💘•**"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "**من ناتوانم ئەدمین میوت بکەم بە جدیتە😂🙂؟**"
        return msg_text, False
    except Exception as e:
        if user_id == 833360381:
            msg_text = "**بۆچی دەتەوێ خۆم میوت؟ نا ببورە من وەکو تۆ گەمژەنیم😂🙂!**"
            return msg_text, False
        
        msg_text = f"**ئۆپسس😂🙂\n{e}**"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)

    msg_text += f"**میوت کرا: {user_mention}\nلەلایەن: {admin_mention}**"
    
    if reason:
        msg_text += f"**هۆکار: `{reason}`\n**"
    if time:
        msg_text += f"**کات: `{time}`\n**"

    return msg_text, True


async def unmute_user(user_id, first_name, admin_id, admin_name, chat_id):
    try:
        await app.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
                can_send_media_messages=True,
                can_send_messages=True,
                can_send_other_messages=True,
                can_send_polls=True,
                can_add_web_page_previews=True,
                can_invite_users=True
            )
        )
    except ChatAdminRequired:
        msg_text = "**ڕۆڵی لادانی میوتکردنم نییە، ڕۆڵی میوتم پێبدە بۆ ئەنجامدانی💘•**"
        return msg_text
    except Exception as e:
        msg_text = f"**ئۆپسس😂🙂\n{e}**"
        return msg_text

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    
    msg_text = f"**میوتی لادرا: {user_mention}\nلەلایەن: {admin_mention}**"
    return msg_text
    


@app.on_message(filters.command(["ban","دەرکردن","باند"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ban_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "**تۆ ڕۆڵت نییە کەسێك دەربکەیت یان باند بکەیت🖤•**"
            return await message.reply_text(msg_text)
    else:
        msg_text = "**تۆ ڕۆڵت نییە کەسێك دەربکەیت یان باند بکەیت🖤•**"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            reason = message.text.split(None, 1)[1]
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("**ناتوانم کەسەکە بدۆزمەوە🖤•**")
                user_id = user_obj[0]
                first_name = user_obj[1]

            try:
                reason = message.text.partition(message.command[1])[2]
            except:
                reason = None

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("**تکایە یوزەری بەکارهێنەر بنووسە لەگەڵ فەرمان یان وەڵامی نامەی ئەو بەکارهێنەرە بدەرەوە🖤•**")
        return
        
    msg_text, result = await ban_user(user_id, first_name, admin_id, admin_name, chat_id, reason)
    if result == True:
        await message.reply_text(msg_text)
    if result == False:
        await message.reply_text(msg_text)


@app.on_message(filters.command(["unban","لادانی دەرکردن","لادانی باند"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def unban_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "**تۆ ڕۆڵت نییە دەرکردن یان باندی کەسێك لابدەیت🖤•**"
            return await message.reply_text(msg_text)
    else:
        msg_text = "**تۆ ڕۆڵت نییە دەرکردن یان باندی کەسێك لابدەیت🖤•**"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        try:
            user_id = int(message.command[1])
            first_name = "User"
        except:
            user_obj = await get_userid_from_username(message.command[1])
            if user_obj == None:
                    return await message.reply_text("**ناتوانم کەسەکە بدۆزمەوە🖤•**")
            user_id = user_obj[0]
            first_name = user_obj[1]

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
    else:
        await message.reply_text("**تکایە یوزەری بەکارهێنەر بنووسە لەگەڵ فەرمان یان وەڵامی نامەی ئەو بەکارهێنەرە بدەرەوە🖤•**")
        return
        
    msg_text = await unban_user(user_id, first_name, admin_id, admin_name, chat_id)
    await message.reply_text(msg_text)




@app.on_message(filters.command(["mute","ئاگاداری","میوت"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def mute_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "**تۆ ڕۆڵت نییە کەسێك میوت بکەیت🖤•**"
            return await message.reply_text(msg_text)
    else:
        msg_text = "**تۆ ڕۆڵت نییە کەسێك میوت بکەیت🖤•**"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            reason = message.text.split(None, 1)[1]
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("**ناتوانم کەسەکە بدۆزمەوە🖤•**")
                user_id = user_obj[0]
                first_name = user_obj[1]

            try:
                reason = message.text.partition(message.command[1])[2]
            except:
                reason = None

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("**تکایە یوزەری بەکارهێنەر بنووسە لەگەڵ فەرمان یان وەڵامی نامەی ئەو بەکارهێنەرە بدەرەوە🖤•**")
        return
    
    msg_text, result = await mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason)
    if result == True:
        await message.reply_text(msg_text)
           
    if result == False:
        await message.reply_text(msg_text)


@app.on_message(filters.command(["لادانی میوت","لادانی ئاگاداری","unmute"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def unmute_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "**تۆ ڕۆڵت نییە میوت یان ئاگاداری کەسێك لابدەیت🖤•**"
            return await message.reply_text(msg_text)
    else:
        msg_text = "**تۆ ڕۆڵت نییە میوت یان ئاگاداری کەسێك لابدەیت🖤•**"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        try:
            user_id = int(message.command[1])
            first_name = "User"
        except:
            user_obj = await get_userid_from_username(message.command[1])
            if user_obj == None:
                    return await message.reply_text("**ناتوانم کەسەکە بدۆزمەوە🖤•**")
            user_id = user_obj[0]
            first_name = user_obj[1]

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
    else:
        await message.reply_text("**تکایە یوزەری بەکارهێنەر بنووسە لەگەڵ فەرمان یان وەڵامی نامەی ئەو بەکارهێنەرە بدەرەوە🖤•**")
        return
        
    msg_text = await unmute_user(user_id, first_name, admin_id, admin_name, chat_id)
    await message.reply_text(msg_text)





@app.on_message(filters.command(["tmute"]))
async def tmute_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "You dont have permission to mute someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to mute someone"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            time = message.text.split(None, 1)[1]

            try:
                time_amount = time.split(time[-1])[0]
                time_amount = int(time_amount)
            except:
                return await message.reply_text("wrong format!!\nFormat: `/tmute 2m`")

            if time[-1] == "m":
                mute_duration = datetime.timedelta(minutes=time_amount)
            elif time[-1] == "h":
                mute_duration = datetime.timedelta(hours=time_amount)
            elif time[-1] == "d":
                mute_duration = datetime.timedelta(days=time_amount)
            else:
                return await message.reply_text("wrong format!!\nFormat:\nm: Minutes\nh: Hours\nd: Days")
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("I can't find that user")
                user_id = user_obj[0]
                first_name = user_obj[1]

            try:
                time = message.text.partition(message.command[1])[2]
                try:
                    time_amount = time.split(time[-1])[0]
                    time_amount = int(time_amount)
                except:
                    return await message.reply_text("wrong format!!\nFormat: `/tmute 2m`")

                if time[-1] == "m":
                    mute_duration = datetime.timedelta(minutes=time_amount)
                elif time[-1] == "h":
                    mute_duration = datetime.timedelta(hours=time_amount)
                elif time[-1] == "d":
                    mute_duration = datetime.timedelta(days=time_amount)
                else:
                    return await message.reply_text("wrong format!!\nFormat:\nm: Minutes\nh: Hours\nd: Days")
            except:
                return await message.reply_text("Please specify a valid user or reply to that user's message\nFormat: `/tmute @user 2m`")

    else:
        await message.reply_text("Please specify a valid user or reply to that user's message\nFormat: /tmute <username> <time>")
        return
    
    msg_text, result = await mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason=None, time=mute_duration)
    if result == True:
        await message.reply_text(msg_text)
    if result == False:
        await message.reply_text(msg_text)


