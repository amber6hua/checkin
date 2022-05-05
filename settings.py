import os

APPROOT = os.path.dirname(os.path.dirname(__file__))

# Telegram credentials
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
PORT = os.environ.get("PORT")
print(API_ID)
print(API_HASH)
print(PORT)

CORS_ORIGINS = [
  'http://localhost:8080',
  'http://127.0.0.1:8080',
  'http://metta-proxy',
  'http://metta-front'
]

if not API_HASH or not API_ID:
    raise SystemExit('API_ID/API_HASH pair not set, check .env file')