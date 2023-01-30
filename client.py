import asyncio
import websockets

async def get_time():
    while True:
        async with websockets.connect("ws://localhost:9090") as websocket:
                print(await websocket.recv())
        await asyncio.sleep(1)

try:
    asyncio.run(get_time())
except KeyboardInterrupt:
    pass