import os
from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from preprocess import normalize_amharic, tokenize_amharic
from config import API_ID, API_HASH, SESSION, CHANNELS
from utils import save_message

client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    msg = event.message
    sender = await msg.get_sender()

    text = msg.message or ""
    cleaned = normalize_amharic(text)
    tokens = tokenize_amharic(cleaned)

    record = {
        "id": msg.id,
        "channel": event.chat.username,
        "sender": sender.username if sender else None,
        "timestamp": msg.date.isoformat(),
        "text": cleaned,
        "tokens": tokens,
        "media_type": None,
        "media_path": None
    }

    if msg.media:
        if isinstance(msg.media, MessageMediaPhoto):
            os.makedirs("media/photos", exist_ok=True)
            path = f"media/photos/{msg.id}.jpg"
            await client.download_media(msg.media, path)
            record["media_type"] = "photo"
            record["media_path"] = path
        elif isinstance(msg.media, MessageMediaDocument):
            os.makedirs("media/docs", exist_ok=True)
            path = f"media/docs/{msg.id}.doc"
            await client.download_media(msg.media, path)
            record["media_type"] = "doc"
            record["media_path"] = path

    save_message(record)
    print(f"📥 {record['channel']}: {cleaned[:50]}...")
