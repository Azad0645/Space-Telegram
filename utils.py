import os
import requests
from dotenv import load_dotenv


load_dotenv()


def get_env_variable(name):
    return os.getenv(name)


def fetch_json(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def download_images(image_urls, folder, prefix="image"):
    os.makedirs(folder, exist_ok=True)
    for i, url in enumerate(image_urls):
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.join(folder, f"{prefix}_{i + 1}.jpg")
        with open(filename, 'wb') as file:
            file.write(response.content)