import os
import time
import random
import argparse
from utils import get_env_variable
from telegram import Bot


def get_args():
    parser = argparse.ArgumentParser(description="Automatic publication of photos in the Telegram channel.")
    parser.add_argument("--folder", type=str, default="nasa_apod_images", help="Folder with photos")
    parser.add_argument("--interval", type=int, default=4 * 60 * 60, help="Photo sending interval in seconds")

    return parser.parse_args()


def get_photo_list(photo_folder):
    photo_list = [os.path.join(photo_folder, f) for f in os.listdir(photo_folder)]
    random.shuffle(photo_list)
    return photo_list


def main():
    args = get_args()

    telegram_token = get_env_variable("TELEGRAM_TOKEN")
    tg_chat_id  = get_env_variable("TG_CHAT_ID")

    bot = Bot(token=telegram_token)

    while True:
        photos = get_photo_list(args.folder)
        for photo in photos:
            with open(photo, 'rb') as file:
                bot.send_photo(chat_id=tg_chat_id, photo=file)
            time.sleep(args.interval)


if __name__ == "__main__":
    main()