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
    parser.add_argument("--chat_id", type=str, default=get_env_variable("CHAT_ID"), help="Telegram channel ID")
    parser.add_argument("--token", type=str, default=get_env_variable("TOKEN"), help="Telegram bot token")

    return parser.parse_args()


def get_photo_list(photo_folder):
    photo_list = [os.path.join(photo_folder, f) for f in os.listdir(photo_folder)]
    random.shuffle(photo_list)
    return photo_list


def main():
    args = get_args()
    bot = Bot(token=args.token)

    while True:
        photos = get_photo_list(args.folder)
        for photo in photos:
            with open(photo, 'rb') as file:
                bot.send_photo(chat_id=args.chat_id, photo=file)
            time.sleep(args.interval)


if __name__ == "__main__":
    main()