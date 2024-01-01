from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from DAXXMUSICimport app
from config import OWNER_ID
from DAXXMUSIC.misc import SUDOERS
from pyrogram.types import Message
from DAXXMUSIC.utils.daxx_ban import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #


@app.on_message(filters.command("pin") & admin_filter & filters.user(SUDOERS))
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**ئەم فەرمانە تەنیا لە گرووپەکان کاردەکات!**")
    elif not replied:
        await message.reply_text("**وەڵامی نامەیەك بدەوە بۆ ئەوەی پینی بکەیت!**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**بە سەرکەوتوویی نامەکە پینکرا!**\n\n**گرووپ:** {chat_title}\n**ئەدمین:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 بینینی نامەکان", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("pinned"))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("**هیچ پینێك نەدۆزرایەوە**")
    try:        
        await message.reply_text("لێرە لیستی هەڵواسراوەکان، پینکراوەکان ببینە",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 بینینی نامەکان",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("unpin") & admin_filter & filters.user(SUDOERS))
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**ئەم فەرمانە تەنیا لە گرووپەکان کاردەکات!**")
    elif not replied:
        await message.reply_text("**وەڵامی نامەیەك بدەوە بۆ ئەوەی لایدەی لە پین!**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"**بە سەرکەوتوویی لە پین لادرا!**\n\n**گرووپ:** {chat_title}\n**ئەدمین:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 بینینی نامەکان ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("removephoto") & admin_filter & filters.user(SUDOERS))
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**پڕۆسەی دەکات ..**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**ئەم فەرمانە تەنیا لە گرووپەکان کاردەکات!**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("**بە سەرکەوتوویی وێنەی گرووپ لابردرا!\nلەلایەن {} **".format(message.from_user.mention))    
      except:
          await msg.edit("**پێویستە ڕۆڵی دەستکاری کردنی زانیاری گرووپت هەبێت بۆ لادانی وێنەی گرووپ**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("setphoto")& admin_filter & filters.user(SUDOERS))
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**پڕۆسەی دەکات . . .**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**ئەم فەرمانە تەنیا لە گرووپەکان کاردەکات!**") 
      elif not reply:
           await msg.edit("**وەڵامی وێنەیەك بدەوە بۆ دانانی لە پڕۆفایلی گرووپ**")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("**بە سەرکەوتوویی وێنەی گرووپ دانرا!\nلەلایەن {}**".format(message.from_user.mention))
             else:
                await msg.edit("**هەندێك جیاوازی و هەڵە ڕوویدا وێنەیەکی تر تاقیبکەوە!**")
     
          except:
              await msg.edit("**پێویستە ڕۆڵی دەستکاری کردنی زانیاری گرووپت هەبێت بۆ دانانی وێنەی گرووپ**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("settitle")& admin_filter & filters.user(SUDOERS))
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**پڕۆسەی دەکات . . .**")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("**ئەم فەرمانە تەنیا لە گرووپەکان کاردەکات!**")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**بە سەرکەوتوویی ناوی گرووپ گۆڕدرا!\nلەلایەن {}**".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("**پێویستە ڕۆڵی دەستکاری کردنی زانیاری گرووپت هەبێت بۆ گۆڕینی ناوی گرووپ!**")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**بە سەرکەوتوویی ناوی گرووپ گۆڕدرا!\nلەلایەن {}**".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("**پێویستە ڕۆڵی دەستکاری کردنی زانیاری گرووپت هەبێت بۆ گۆڕینی ناوی گرووپ!**")
          

    else:
       await msg.edit("**پێویستە وڵامی ئەو ناوە بدەیتەوە یان لەگەڵ فەرمان بینووسی بۆ ئەوەی ناوی گرووپ بگۆڕێت!**")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command("setdiscription") & admin_filter & filters.user(SUDOERS))
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ...**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘs!**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ ɪɴsᴇʀᴛ!**\nʙʏ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**ᴛʜᴇ ᴜsᴇʀ ᴍᴜsᴛ ʜᴀᴠᴇ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ!**")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ ɪɴsᴇʀᴛ!**\nʙʏ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**ᴛʜᴇ ᴜsᴇʀ ᴍᴜsᴛ ʜᴀᴠᴇ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ!**")
    else:
        await msg.edit("**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛᴏɴ!**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("lg")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**sᴜᴄᴄᴇssғᴜʟʟʏ ʜɪʀᴏ !!.**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


# --------------------------------------------------------------------------------- #


