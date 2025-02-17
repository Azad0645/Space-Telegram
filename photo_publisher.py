import os
import time
import random
import argparse
from dotenv import load_dotenv
from telegram import Bot


def get_args():
    parser = argparse.ArgumentParser(description="Automatic publication of photos in the Telegram channel.")
    parser.add_argument("--folder", type=str, default="nasa_apod_images", help="Folder with photos")
    parser.add_argument("--interval", type=int, default=4 * 60 * 60, help="Photo sending interval in seconds")
    parser.add_argument("--token", type=str, default=os.getenv("TELEGRAM_TOKEN"), help="Telegram bot token")
    parser.add_argument("--chat_id", type=str, default=os.getenv("TG_CHAT_ID"), help="Telegram chat ID")

    return parser.parse_args()


def get_photos(folder):
    photos  = [os.path.join(folder, f) for f in os.listdir(folder)]
    random.shuffle(photos)
    return photos


def main():
    load_dotenv()

    args = get_args()

    bot = Bot(token=args.token)

    while True:
        photos = get_photos(args.folder)
        for photo in photos:
            with open(photo, 'rb') as file:
                bot.send_photo(chat_id=args.chat_id, photo=file)
            time.sleep(args.interval)


if __name__ == "__main__":
    main()