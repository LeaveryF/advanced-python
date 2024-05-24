#!/usr/bin/env python

# 没有做到实时接收请求



import asyncio
import websockets
import queue

async def handle_client(websocket, path):
    print("Connected")
    priority_queue = queue.PriorityQueue()

    try:
        while True:
            # 接收客户端发送的整数
            num = int(await websocket.recv())
            print("<<<", num)

            # 将整数添加到优先队列中
            priority_queue.put(num)

            # 每隔1秒钟取出优先队列中最大的数并发送给客户端
            if priority_queue.qsize() > 0:
                max_num = priority_queue.get()
                message = f"<{priority_queue.qsize()},{max_num}>"
                # websocket send 的数据 必须是字符串类型
                await websocket.send(message)
                print(">>>", message)
            else:
                message = f"<{0},None>"
                await websocket.send(message)
                print(">>>", message)

            # 等待1秒钟
            await asyncio.sleep(1)

    except websockets.ConnectionClosed:
        print("Connection closed")

start_server = websockets.serve(handle_client, "localhost", 1234)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
