import asyncio
import websockets
import datetime

async def send_localtime(websocket):
        
    date_time = datetime.datetime.now()
    date_time = "[%d %02d %02d]\t%02d:%02d:%02d" % (date_time.year, date_time.day, date_time.month, date_time.hour, date_time.minute, date_time.second)
    await websocket.send(date_time)
    
async def main():
    print("Server Is UP!")
    async with websockets.serve(send_localtime, "localhost", 9090):
        await asyncio.Future()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass