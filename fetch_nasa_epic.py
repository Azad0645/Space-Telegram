import argparse
from utils import fetch_json, download_images, get_env_variable


API_KEY = get_env_variable("NASA_API_KEY")


def get_epic_image_urls(api_key, count=5):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {"api_key": api_key}
    json_response = fetch_json(url, params=params)

    image_urls = []
    for item in json_response[:count]:
        date = item['date'].split(" ")[0]
        year, month, day = date.split("-")
        image_name = item['image']
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/jpg/{image_name}.jpg"
        image_urls.append(image_url)

    return image_urls


def main():
    parser = argparse.ArgumentParser(description="Fetch NASA EPIC images.")
    parser.add_argument("--count", type=int, default=5, help="Number of EPIC images to fetch")
    parser.add_argument("--folder", type=str, default="epic_images", help="Folder to save NASA EPIC images")
    args = parser.parse_args()


    image_urls = get_epic_image_urls(api_key=API_KEY, count=args.count)
    download_images(image_urls, folder=args.folder, prefix="epic")


if __name__ == "__main__":
    main()