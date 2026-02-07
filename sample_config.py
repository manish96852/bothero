import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Check if running on cloud (Heroku/Render) or locally
HEROKU = os.environ.get("HEROKU", "False") == "True"

if HEROKU:
    # Cloud deployment - use environment variables
    try:
        API_ID = int(os.environ["API_ID"])
        API_HASH = os.environ["API_HASH"]
        SESSION_STRING = os.environ["SESSION_STRING"]
        CHAT_ID = int(os.environ["CHAT_ID"])
    except KeyError as e:
        print(f"❌ ERROR: Missing environment variable: {e}")
        print("Please set all required environment variables in your deployment platform:")
        print("- API_ID")
        print("- API_HASH")
        print("- SESSION_STRING")
        print("- CHAT_ID")
        exit(1)
else:
    # Local deployment - fill these values manually
    API_ID = 12345678  # Get from my.telegram.org/apps
    API_HASH = "your_api_hash"  # Get from my.telegram.org/apps
    SESSION_STRING = "your_session_string"  # Generate using generate_string_session.py
    CHAT_ID = -1001234567890  # Your group chat ID (use @userinfobot)
