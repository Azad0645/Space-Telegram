import argparse
from utils import fetch_json, download_images, get_env_variable


API_KEY = get_env_variable("NASA_API_KEY")


def get_apod_images(api_key, count=30):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "count": count}
    data = fetch_json(url, params=params)
    return [item['url'] for item in data if item['media_type'] == 'image']


def main():
    parser = argparse.ArgumentParser(description="Fetch NASA APOD images.")
    parser.add_argument("--count", type=int, default=30, help="Number of APOD images to fetch")
    parser.add_argument("--folder", type=str, default="nasa_apod_images", help="Folder to save NASA APOD images")
    args = parser.parse_args()


    image_urls = get_apod_images(api_key=API_KEY, count=args.count)
    download_images(image_urls, folder=args.folder, prefix="apod")


if __name__ == "__main__":
    main()