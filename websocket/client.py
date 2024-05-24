#!/usr/bin/env python

# * 也可以使用client.html进行测试 其中由浏览器运行了js代码

import asyncio
import websockets
# 否则将被input语句阻塞
import aioconsole

async def recv_data(websocket):
    while True:
        receive = await websocket.recv()
        print(f"<<< {receive}")

async def send_data(websocket):
    aiocli = aioconsole.AsynchronousCli([])
    while True:
        message = await aiocli.ainput("Input a string: ")
        await websocket.send(message)
        print(f">>> {message}")

# async def send_data(websocket):
#     while True:
#         message = await asyncio.get_event_loop(None, input, "Input a string: ")
#         await websocket.send(message)
#         print(f">>> {message}")

async def echo():
    uri = "ws://localhost:1234/echo"
    async with websockets.connect(uri) as websocket:
        await asyncio.gather(recv_data(websocket), send_data(websocket))



# async def recv_data(websocket):
#     while True:
#         receive = await websocket.recv()
#         print(f"<<< {receive}")

# async def echo():
#     uri = "ws://localhost:1234/echo"
#     async with websockets.connect(uri) as websocket:
#         asyncio.create_task(recv_data(websocket))
#         while True:
#             message = input("Input a string: ")

#             await websocket.send(message)
#             print(f">>> {message}")



# async def echo():
#     uri = "ws://localhost:1234/echo"
#     async with websockets.connect(uri) as websocket:
#         while True:
#             message = input("Input a string: ")

#             await websocket.send(message)
#             print(f">>> {message}")

#             receive = await websocket.recv()
#             print(f"<<< {receive}")

if __name__ == "__main__":
    asyncio.run(echo())
