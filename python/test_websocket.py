import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        if message == "hello":
            print("Received hello from the client!")

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
