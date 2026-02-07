# Telegram Voice Chat Join Notifier Bot

Simple Telegram bot that sends a message in your group whenever someone joins the voice chat.

## Features

🎤 **Voice Chat Join Notifications** - Automatically sends "🎤 **[Name]** joined the voice chat!" message when someone joins

## Requirements

### Account requirements
- A Telegram user account (not a bot account)
- API_ID and API_HASH from [my.telegram.org](https://my.telegram.org)
- Session string for the account

### Environment requirements
- Python 3.9 or later
- pip3

## Installation & Setup

### 1. Clone the repository

```sh
$ git clone https://github.com/yourusername/Telegram_VC_Bot
$ cd Telegram_VC_Bot
```

### 2. Install requirements

```sh
$ pip3 install -U pip
$ pip3 install -U -r requirements.txt
```

### 3. Generate Session String

```sh
$ pip3 install pyrogram TgCrypto
$ python3 generate_string_session.py
```

Follow the prompts to generate your session string.

### 4. Configure the bot

Copy the sample config:
```sh
$ cp sample_config.py config.py
```

Edit **config.py** with your values:
- `API_ID` - Your Telegram API ID
- `API_HASH` - Your Telegram API Hash
- `SESSION_STRING` - The session string you generated
- `CHAT_ID` - Your group chat ID (can be found using @userinfobot)
- Set `HEROKU = False` if running locally

### 5. Run the bot

```sh
$ python3 main.py
```

## Docker Deployment

```sh
$ git clone https://github.com/yourusername/Telegram_VC_Bot && cd Telegram_VC_Bot
$ cp sample.env .env
```

Edit **.env** with your values.

```sh
$ sudo docker build . -t tgvc-notifier
$ sudo docker run tgvc-notifier
```

To stop use `CTRL+C`

## Heroku Deployment

1. Fork this repository
2. Generate your session string using `generate_string_session.py`
3. Click the deploy button below and fill in the required environment variables

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Commands

Command | Description
:--- | :---
/start | Check if bot is active

## How It Works

The bot monitors voice chat events in your specified group. When someone joins the voice chat, it automatically sends a notification message with their name.

## Notes

- The bot needs to be added to your group
- Make sure to get the correct CHAT_ID (use @userinfobot in your group)
- The session string grants access to your Telegram account, keep it secure

## Credits

Based on the original Telegram_VC_Bot project
