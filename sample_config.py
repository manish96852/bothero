HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ
    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ["SESSION_STRING"]  # Check Readme for session
    CHAT_ID = int(environ["CHAT_ID"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 12345678
    API_HASH = "your_api_hash"
    SESSION_STRING = "your_session_string"
    CHAT_ID = -1001234567890  # Your group chat ID
