import argparse
from utils import fetch_api_data, download_images


def get_spacex_image_urls(launch_id="latest"):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = fetch_api_data(url)
    return response['links']['flickr']['original']


def main():
    parser = argparse.ArgumentParser(description="Fetch SpaceX launch images.")
    parser.add_argument("--launch_id", type=str, default="latest", help="ID of the SpaceX launch")
    parser.add_argument("--folder", type=str, default="spacex_images", help="Folder to save SpaceX images")
    args = parser.parse_args()


    photos = get_spacex_image_urls(launch_id=args.launch_id)
    download_images(photos, folder=args.folder, prefix="spacex_photo")


if __name__ == "__main__":
    main()