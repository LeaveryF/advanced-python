import asyncio
import websockets

async def receive_data(websocket):
    while True:
        # 接收服务器发送的数据
        server_data = await websocket.recv()
        print(f"从服务器接收到的数据： {server_data}")

async def send_data(websocket):
    while True:
        # 接收实时输入的数据并发送
        user_input = input("请输入要发送的数据： ")
        await websocket.send(user_input)

async def websocket_client():
    uri = "ws://localhost:1234/echo"
    async with websockets.connect(uri) as websocket:
        await asyncio.gather(receive_data(websocket), send_data(websocket))

asyncio.get_event_loop().run_until_complete(websocket_client())