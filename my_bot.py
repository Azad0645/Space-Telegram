from telegram import Bot
from dotenv import load_dotenv
import os
import random


load_dotenv()
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


PHOTO_FOLDER = 'epic_images'
PHOTO_PATH = 'epic_images/epic_1.jpg'


if not PHOTO_PATH:
    PHOTO_PATH = os.path.join(PHOTO_FOLDER, random.choice(os.listdir(PHOTO_FOLDER)))


bot = Bot(token=TOKEN)


with open(PHOTO_PATH, 'rb') as photo:
    bot.send_photo(chat_id=CHAT_ID, photo=photo)
