from telegram import Bot
from utils import get_env_variable
import os
import random


TOKEN = get_env_variable("TOKEN")
CHAT_ID = get_env_variable("CHAT_ID")


def main():
    photo_folder = 'epic_images'
    photo_path = 'epic_images/epic_1.jpg'

    if not  photo_path:
        photo_path = os.path.join(photo_folder, random.choice(os.listdir(photo_folder)))

    bot = Bot(token=TOKEN)

    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=CHAT_ID, photo=photo)


if __name__ == "__main__":
    main()