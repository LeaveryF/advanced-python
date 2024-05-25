#!/usr/bin/env python

# 仍然未能实现 因为asyncio

# 功能：
# 运行python脚本将连接并访问ws://localhost:1234/echo建立websocket连接
# 建立连接后 客户端每秒收到一个来自服务器的消息<最大数字, 优先队列长度>
# 客户端可随时发送一条包含一个数字消息给服务器以更新服务器端的优先队列信息
# 因为服务器端暂未进行错误处理 不要输入错误的数据 尽管这样将输入和输出混合的界面确实不太友好
# 不使用asyncio库 使用多线程分别实现发送和接收
# 目前程序是死循环 需要退出时可能不得不Ctrl-C

# * 也可以使用client.html进行测试 其中由浏览器运行了js代码

# * 也可以使用client.js进行测试
# * 测试方法：chrome浏览器 检查/开发者工具/F12 - 源代码/来源 - 工作区/代码段

import asyncio
import websockets
from threading import Thread

import time

# 接收线程
async def recv_data(websocket):
    while True:
        message = await websocket.recv()
        print("<<<", message)
        time.sleep(10)

# 发送线程
async def send_data(websocket):
    while True:
        message = input() # 输入数据时只管输入就好
        await websocket.send(message)

async def echo():
    uri = "ws://localhost:1234/echo"
    async with websockets.connect(uri) as websocket:
        # 创建线程 参数元组包含websocket
        recv_thread = Thread(target=recv_data, name="recv_thread", args=(websocket,))
        send_thread = Thread(target=send_data, name="send_thread", args=(websocket,))
        
        # 启动线程
        recv_thread.start()
        send_thread.start()

        # 等待线程结束 当然实际上不会结束
        recv_thread.join()
        send_thread.join()

if __name__ == "__main__":
    asyncio.run(echo())
