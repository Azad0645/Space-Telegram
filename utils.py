import os
import requests


def fetch_api_data(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def download_images(image_urls, folder, prefix="image"):
    os.makedirs(folder, exist_ok=True)
    for image_number, image_url in enumerate(image_urls, start=1):
        response = requests.get(image_url)
        response.raise_for_status()
        filename = os.path.join(folder, f"{prefix}_{image_number}.jpg")
        with open(filename, 'wb') as file:
            file.write(response.content)