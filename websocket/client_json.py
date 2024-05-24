#!/usr/bin/env python

# 也可以使用client.js进行测试
# 测试方法：chrome浏览器 检查/开发者工具/F12 - 源代码/来源 - 工作区/代码段

import asyncio
import websockets
import json

async def echo():
    uri = "ws://localhost:1234"
    cnt = 0
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Input a string: ")

            request = {'number': cnt, 'message': message}
            cnt += 1
            await websocket.send(json.dumps(request))
            print(f">>> {request}")

            receive = await websocket.recv()
            print(f"<<< {json.loads(receive)}")

if __name__ == "__main__":
    asyncio.run(echo())