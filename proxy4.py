#!/usr/bin/env python3

import asyncio
import websockets
import socket
import _thread

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
init_message = '(dispinit version 5)'
udp.sendto(init_message.encode('utf-8'), ('127.0.0.1', 6000))


async def web(websocket):
    msg = await websocket.recv()


async def serve(websocket):
    while True:
        message = udp.recv(40960).decode('utf-8')[:-1]
        await(websocket.send(message))


async def main():
    async with websockets.serve(serve, 'localhost', 7000):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
