import json

import asyncio
import websockets

from ppt.ppt import PPT
from util.json_encoder import BaseEncoder


async def send(websocket, slide):
    print("发送")
    await websocket.send(json.dumps(slide, cls=BaseEncoder, ensure_ascii=False))


async def handler(websocket):
    while True:
        data = await websocket.recv()
        print("topic", data)
        ppt = PPT()
        await ppt.generate_ppt(topic=data,
                               websocket=websocket,
                               slide_finish=send)


# start a websocket server
server = websockets.serve(handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()  # run forever

# PPT("年轻人为什么不结婚")
