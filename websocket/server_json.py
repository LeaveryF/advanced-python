#!/usr/bin/env python

import asyncio
import websockets
import json

# json.dumps()将python对象转化为json字符串
# json.loads()将json字符串转化为python对象
'''
>>> print(json.dumps({'a':1,'b':2})) 
{"a": 1, "b": 2}
>>> print(json.loads('{"a":1,"b":2}')) 
{'a': 1, 'b': 2}
'''
# 因此实际上 传json数据传的本质上就是字符串而已

# async 是一个关键字，用于声明一个函数为异步函数，即所谓的协程
# 当一个函数被async修饰后，它将返回一个协程对象而不是直接执行
async def echo(websocket, path):
    try:
        while True:
            # await 也是一个关键字，用在协程函数内部，它可以暂停当前协程的执行，等待另一个协程完成它的任务，然后再继续执行后面的代码
            message = await websocket.recv()
            print(f"<<< {json.loads(message)}")

            message = f"\"{json.loads(message)}\" has received by server: \"ws://localhost:1234{path}\""
            response = {'status': 'success', 'message': message}
            await websocket.send(json.dumps(response))
            print(f">>> {response}")
    except websockets.exceptions.ConnectionClosedOK:
        print("A client disconnected")

async def main():
    # websockets.serve的第一个参数 handler: 
    # 这是一个处理 WebSocket 连接的异步函数
    # 该函数接收两个参数：websocket 和 path
    # websocket 是一个 WebSocket 连接对象，可以用来发送和接收消息
    # path 是客户端请求的路径
    async with websockets.serve(echo, "localhost", 1234):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

# 另一种方法

# # 启动WebSocket服务器
# start_server = websockets.serve(echo, "localhost", 1234)

# # 运行服务器
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()