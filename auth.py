import os
import time
from telethon import TelegramClient, events, sync
import asyncio
from settings import API_HASH, API_ID, DATABASE_URL
from alchemysession import AlchemySessionContainer
container = AlchemySessionContainer(DATABASE_URL)


# 第一次登录时需要输入手机号和登录验证码，会在此文件同目录下生成
# bot_name.session，后续依靠这个文件不再需要重新登录

def auth():
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)

    session_name = "id_" + API_ID + '.session'
    session = container.new_session(session_name)
    client = TelegramClient(session, API_ID, API_HASH)
    # client.connect()
    client.start()
    client.disconnect()
    return


if __name__ == '__main__':
    auth()
