from telegram import Bot
from utils import get_env_variable
import os
import random


TOKEN = get_env_variable("TOKEN")
CHAT_ID = get_env_variable("CHAT_ID")


PHOTO_FOLDER = 'epic_images'
PHOTO_PATH = 'epic_images/epic_1.jpg'


if not PHOTO_PATH:
    PHOTO_PATH = os.path.join(PHOTO_FOLDER, random.choice(os.listdir(PHOTO_FOLDER)))


bot = Bot(token=TOKEN)


with open(PHOTO_PATH, 'rb') as photo:
    bot.send_photo(chat_id=CHAT_ID, photo=photo)
