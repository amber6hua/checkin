from settings import API_HASH, API_ID, DATABASE_URL
from telethon import TelegramClient
from alchemysession import AlchemySessionContainer
container = AlchemySessionContainer(DATABASE_URL, None, '', None, False)

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

        session = container.new_session(self._session)
        client = TelegramClient(session, API_ID, API_HASH)
        # return TelegramClient(self._session, API_ID, API_HASH)
        return client
