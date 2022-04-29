from settings import API_HASH, API_ID
from telethon import TelegramClient

class SessionConfig:

    def __init__(self, file_path):
        self._session = file_path

    async def conn(self):
        print(self.client.is_connected())
        if not self.client.is_connected():
            await self.client.connect()
        return self.client

    @property
    def client(self) -> TelegramClient:
        if not self._session:
            raise SystemExit('not authorized!')
        host = "127.0.0.1"
        port = 10808
        proxy = (socks.SOCKS5, host, port)
        return TelegramClient(self._session, API_ID, API_HASH, proxy=proxy)
