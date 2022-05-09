import os

APPROOT = os.path.dirname(os.path.dirname(__file__))

# Telegram credentials
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
PORT = os.environ.get("PORT")
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_URL = DATABASE_URL.replace('postgres', 'postgresql')

if not API_HASH or not API_ID:
    raise SystemExit('API_ID/API_HASH pair not set, check .env file')