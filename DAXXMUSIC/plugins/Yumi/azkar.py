import random
import asyncio
from strings.filters import command
from DAXXMUSIC import app
from pyrogram import Client, filters
import requests


@app.on_message(command(["کردنەوەی زکر"]))
async def enable_azkar(client, message):
    chat_id = message.chat.id
    if chat_id not in Tom:
        Tom.append(chat_id)
        await message.reply_text("**بە سەرکەوتوویی فەرمانی زکر کرایەوە♥️✅•**")
        return
    await message.reply_text("**زکر پێشتر کراوەتەوە♥️✅•**")

@app.on_message(command(["داخستنی زکر"]))
async def disable_azkar(client, message):
    chat_id = message.chat.id
    if chat_id in Tom:
        Tom.remove(chat_id)
        await message.reply_text("**بە سەرکەوتوویی فەرمانی زکر داخرا♥️❎•**")
        return
    await message.reply_text("**زکر پێشتر داخراوە♥️❎•**")


async def send_random_azkar():
    while True:
        url = "http://azkartom.dev-tomtom.repl.co"
        response = requests.get(url)
        data = response.json()
        tooom = data["Tom"]
        random_azkar = random.choice(tooom)
        content = random_azkar["content"]
        if content not in azkaary:
            for ahmed in Tom:
            	await app.send_message(ahmed, text=content)
            	azkaary.append(content)
            	if len(azkaary) >= 120:
            		azkaary.clear()
            
        await asyncio.sleep(600)  #کاتەکەی

