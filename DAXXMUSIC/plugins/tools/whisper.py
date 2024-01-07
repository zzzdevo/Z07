from pyrogram import Client, filters, idle
from pyrogram.types import InlineQueryResultPhoto, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from pyrogram import enums
from DAXXMUSIC import app as app

######################
LOG = -1001834002030 #
######################

@app.on_message(filters.command("wstart") & filters.private)
async def startmsg(app, message):
   text = '''**
👋 سڵاو {}

❓ چۆن چرپە بەکاربێنم :

`@IQMCBOT سلاو @IQ7amo`
`@IQMCBOT سلاو @all`

**'''.format(message.from_user.mention)
   key = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ("تاقیکردنەوە", switch_inline_query='سلاو @IQ7amo') ]]
   )
   await message.reply(text, reply_markup=key, quote=True)


@app.on_inline_query(filters.regex("@"))
async def whisper(app, iquery):
    user = iquery.query.split("@")[1]
    if " " in user: return 
    user_id = iquery.from_user.id
    query = iquery.query.split("@")[0]
    if user == "all":
      text = "**🎊 ئەم چرپەیە بۆ هەمووانە**"
      username = "all"
    else:
      get = await app.get_chat(user)
      user = get.id
      username = get.first_name
      text = f"**🔒 چرپەیەك بۆ ( {username} ) **"
    send = await app.send_message(LOG, query)
    reply_markup = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("📪 پیشاندانی نامە", callback_data=f"{send.id}هێنان{user}from{user_id}")
      ]]
    )
    await iquery.answer(
      results=[
       InlineQueryResultArticle(
          title=f"**📪 چرپەنامەیەكت نارد بۆ {username}**",
          url="http://t.me/MGIMT",
          input_message_content=InputTextMessageContent(
            message_text=text,
            parse_mode=enums.ParseMode.MARKDOWN 
          ),
          reply_markup=reply_markup
       )
      ],
      cache_time=1
    )

@app.on_inline_query()
async def whisper(app, query):
    text = '''**
❓ چۆن چرپە بەکاربێنم :

`@IQMCBOT سلاو @IQ7amo`
`@IQMCBOT سلاو @all`

**'''
    await query.answer(
        results=[
            InlineQueryResultPhoto(
                title="🔒 چرپەنامە لەگەڵ + یوزەر",
                photo_url='https://graph.org/file/7a3defa398f4ce6a0a055.jpg',
                description='@IQMCBOT سەرۆکی بۆت @IQ7amo',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🔗", url='t.me/MGIMT')]]),
                input_message_content=InputTextMessageContent(text)
            ),
        ],
        cache_time=1
    )
    
@app.on_callback_query(filters.regex("هێنان"))
async def get_whisper(app,query):
    sp = query.data.split("هێنان")[1]
    user = sp.split("from")[0]
    from_user = int(sp.split("from")[1])
    reply_markup = InlineKeyboardMarkup(
      [
      [
        InlineKeyboardButton("📪 پیشاندانی نامە", callback_data=query.data)
      ],
      [
        InlineKeyboardButton("🗑️", callback_data=f"DELETE{from_user}")
      ],
      ]
    )
    if user == "all":
       msg = await app.get_messages(LOG, int(query.data.split("هێنان")[0]))
       await query.answer(msg.text, show_alert=True)
       try:
         await query.edit_message_reply_markup(
           reply_markup
         )
       except:
         pass
       try:
         alert0 = f"📭 {query.from_user.mention} کرایەوە @all چرپەنامە"
         await app.send_message(from_user, alert0)
       except:
         pass
       return 
    
    else:
      if str(query.from_user.id) == user:
        msg = await app.get_messages(LOG, int(query.data.split("هێنان")[0]))
        await query.answer(msg.text, show_alert=True)
        try:
         await query.edit_message_reply_markup(
           reply_markup
         )
        except:
         pass
        return 

      if query.from_user.id == from_user:
        msg = await app.get_messages(LOG, int(query.data.split("هێنان")[0]))
        await query.answer(msg.text, show_alert=True)
        return
      
      else:
        get = await app.get_chat(int(user))
        touser = get.first_name
        alert = f"**کەسێك هەوڵیدا چرپەی تۆ بکاتەوە {touser}:\n\n**"
        alert += f"👤 ناو : {query.from_user.mention}\n"
        alert += f"🆔 ئایدی : {query.from_user.id}\n"
        if query.from_user.username:
          alert += f"🔍 یوزەر : @{query.from_user.username}\n"
        alert += "\n\n📭"
        await query.answer("🔒 ئەم چرپەیە بۆتۆ نییە بەڕێزم", show_alert=True)
        try:
          await app.send_message(
            from_user,
            alert
          )
        except:
          pass
        return 

@app.on_callback_query(filters.regex("DELETE"))
async def del_whisper(app,query):
   user = int(query.data.split("DELETE")[1])
   if not query.from_user.id == user:
     return await query.answer("❓ تەنیا ئەو کەسە دەتوانێت کە ناردوویەتی")
   
   else:
     reply_markup = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("خاوەنی بۆت", url="https://t.me/IQ7amo")
      ]]
    )
     await query.edit_message_text(f"**🗑️ چرپەنامە سڕدرایەوە لە لایەن: ( {query.from_user.mention} )**",
       reply_markup=reply_markup
     )
     
idle()
