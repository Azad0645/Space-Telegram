import os
import random
import argparse
from dotenv import load_dotenv
from telegram import Bot


def get_args():
    parser = argparse.ArgumentParser(description="Send a photo to a Telegram channel.")
    parser.add_argument("--photo", type=str, help="Path to the photo")
    parser.add_argument("--folder", type=str, default="epic_images", help="Folder with images (if no photo specified)")
    return parser.parse_args()


def main():
    load_dotenv()

    telegram_token = os.getenv("TELEGRAM_TOKEN")
    tg_chat_id = os.getenv("TG_CHAT_ID")

    args = get_args()

    if args.photo:
        photo_path = args.photo
    else:
        photo_folder = args.folder
        photo_path = os.path.join(photo_folder, random.choice(os.listdir(photo_folder)))

    bot = Bot(token=telegram_token)

    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=tg_chat_id, photo=photo)


if __name__ == "__main__":
    main()