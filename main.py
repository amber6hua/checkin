from telethon import TelegramClient
from quart import Quart, request
from quart_cors import route_cors
import hypercorn
from hypercorn.asyncio import serve
import asyncio
import json
from settings import API_HASH, API_ID
from session import SessionConfig

session = SessionConfig('id_' + API_ID + '.session')
client = session.client

# Telethon Client And Proxy
# host = "127.0.0.1"
# port = 10808
# proxy = (socks.SOCKS5, host, port)
# client = TelegramClient('id_' + API_ID, API_ID, API_HASH, proxy=proxy)

# Quart App
app = Quart(__name__)
app.secret_key = 'CHANGE THIS TO SOMETHING SECRET'

loop = asyncio.get_event_loop()


# Connect the client before we start serving with Quart

@app.before_serving
async def startup():
    await client.connect()


# After we're done serving (near shutdown), clean up the client

@app.after_serving
async def cleanup():
    await client.disconnect()


@app.route('/', methods=["GET"])
@route_cors(
    allow_origin=["http://localhost:3000"])
async def hello():
    return "Hello World"


@app.route('/requestCode', methods=["POST"])
@route_cors(allow_headers=["content-type"],
            allow_methods=["POST"], allow_origin=["http://localhost:3000"])
async def sendCode():
    data = await request.get_json()
    global phone
    phone = data["phone"]
    if 'phone' in data:
        try:
            await client.send_code_request(phone)
        except:
            return "Phone Number incorrect", 400
        return "Code Sent", 201


@app.route('/signin', methods=["POST"])
@route_cors(allow_headers=["content-type"],
            allow_methods=["POST"],
            allow_origin=["http://localhost:3000"])
async def signInAttempt():
    data = await request.get_json()
    code = data["code"]
    global phone

    if not await client.is_user_authorized():
        if 'code' in data:
            try:
                await client.sign_in(phone, code)
            except:
                return "Unauthorized", 401
            me = await client.get_me()

            response = {}
            response["id"] = me.id
            response["username"] = me.username
            response["access_hash"] = me.access_hash
            response["first_name"] = me.first_name
            response["last_name"] = me.last_name
            response["phone"] = me.phone
            json_data = json.dumps(response, ensure_ascii=False)

            return json_data, 200
    return "Already Logged in", 406


@app.route('/logout', methods=["POST"])
@route_cors(allow_headers=["content-type"],
            allow_methods=["POST"],
            allow_origin=["http://localhost:3000"])
async def logout():
    try:
        await client.log_out()
    except:
        return "Logout failed", 401

    return "Logout Success", 200


config = hypercorn.Config()
config.bind = ["0.0.0.0:8080"]
loop.run_until_complete(serve(app, config))
