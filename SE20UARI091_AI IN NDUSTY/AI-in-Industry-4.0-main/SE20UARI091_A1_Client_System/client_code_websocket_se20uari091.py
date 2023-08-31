#Write a Program in python to send a message from client system to server system and vice versa.

#Use the library websocket.

import websockets
import asyncio

async def listen():
    url = "ws://123.115.258.113:5006"
    async with websockets.connect(url) as websocket:
        await websocket.send("Hello Server!")
        while True:
            message = await websocket.recv()
            print(message)

asyncio.get_event_loop().run_until_complete(listen())

