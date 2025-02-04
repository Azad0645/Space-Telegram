# Space Telegram

Project description:
- This bot automatically publishes photos from NASA, SpaceX and EPIC to your Telegram channel at a specified interval. 

## How to install and launch

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

Launch the bot:
- `python photo_publisher.py`

## Project goal

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org).