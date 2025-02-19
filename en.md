# Space Telegram

Project description:
- This bot automatically publishes photos from NASA, SpaceX and EPIC to your Telegram channel at a specified interval. 

## How to install 

Create a bot in Telegram:
- Go to Telegram and write to the bot @BotFather.
- Get TOKEN - you will need it for the bot to work.
- Add a bot to your channel and give it administrator rights.
- Find out the CHAT_ID of the channel

Create .env file in the project root folder and add your token and channel ID there:
- TOKEN=your token
- CHAT_ID=channel name

Installing dependencies:
- Python 3 must already be installed.
- `pip install -r requirements.txt`

## Examples of running all scripts

Automatic publication of photos every 4 hours:
-  `python photo_publisher.py`

Sending one photo (specified or random):
- `python send_photo.py --photo "epic_images/epic_1.jpg"`
- `python send_photo.py`

Uploading photos from NASA APOD:
- `python fetch_nasa_apod.py`

Uploading EPIC photos:
- `python fetch_nasa_epic.py`

Uploading SpaceX photos:
- `python fetch_spacex_images.py`

## Project goal

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org).