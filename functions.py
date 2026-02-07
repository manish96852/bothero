import os
from pyrogram import Client

is_config = os.path.exists("config.py")

if is_config:
    from config import *
else:
    from sample_config import *

app = Client(
    SESSION_STRING if HEROKU else "tgvc",
    api_id=API_ID,
    api_hash=API_HASH,
)

