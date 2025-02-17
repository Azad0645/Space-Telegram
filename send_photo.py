from telegram import Bot
from dotenv import load_dotenv
import os
import random


def main():
    load_dotenv()

    telegram_token = os.getenv("TELEGRAM_TOKEN")
    tg_chat_id = os.getenv("TG_CHAT_ID")

    photo_folder = 'epic_images'
    photo_path = 'epic_images/epic_1.jpg'

    if not  photo_path:
        photo_path = os.path.join(photo_folder, random.choice(os.listdir(photo_folder)))

    bot = Bot(token=telegram_token)

    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=tg_chat_id, photo=photo)


if __name__ == "__main__":
    main()