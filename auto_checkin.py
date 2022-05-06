import os
import time
from telethon import TelegramClient, events, sync
import asyncio
from settings import API_HASH, API_ID, DATABASE_URL
from alchemysession import AlchemySessionContainer
container = AlchemySessionContainer(DATABASE_URL, None, '', None, False)


# 第一次登录时需要输入手机号和登录验证码，会在此文件同目录下生成
# bot_name.session，后续依靠这个文件不再需要重新登录

def checkin():
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)

    api_id = [API_ID]  # 输入api_id，一个账号一项
    api_hash = [API_HASH]  # 输入api_hash，一个账号一项
    robot_map = {'@yyjc_checkin_bot': '/checkin'}
    session_name = api_id[:]
    for num in range(len(api_id)):
        session_name[num] = "id_" + str(session_name[num] + '.session')

        session = container.new_session(session_name[num])
        client = TelegramClient(session, api_id[num], api_hash[num])
        # client = TelegramClient(session_name[num], api_id[num], api_hash[num])
        client.connect()
        # client.start()
        for (k, v) in robot_map.items():
            print("Start checkin: ", k)
            client.send_message(k, v)  # 设置机器人和签到命令
            time.sleep(3)
            client.send_read_acknowledge(k)  # 将机器人回应设为已读
            print("Done! Session name:", session_name[num])

    client.disconnect()
    return


if __name__ == '__main__':
    checkin()
