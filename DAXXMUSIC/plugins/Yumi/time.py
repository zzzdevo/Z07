from pyrogram import Client, filters
from datetime import datetime
import pytz
from strings.filters import command
from DAXXMUSIC import app


def get_current_time():
    tz = pytz.timezone('Asia/Baghdad')  # Setting the timezone to India (Kolkata)
    current_time = datetime.now(tz)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

@app.on_message(command(["/Time","کات"]))
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"**کاتی کوردستان: {time}**")
