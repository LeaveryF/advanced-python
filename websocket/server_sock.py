#!/usr/bin/env python

# flask_socketio:
# flask_socketio是一个成熟的库，它为Flask提供了完整的Socket.IO支持。
# 它提供了自动重连、事件广播、命名空间、房间等高级特性，这些特性使得实现实时通信变得非常简单。
# flask_socketio还提供了与Flask应用集成紧密的API，例如使用Flask的蓝图（Blueprints）来组织Socket.IO路由。
# 它适用于需要复杂实时交互的应用，如聊天应用、游戏或任何需要推送/拉取大量实时数据的场景。

# flask_sock:
# flask_sock是一个较新的库，它提供了一个更简单的接口来实现基本的WebSocket功能。
# 它没有flask_socketio那么多高级特性，但它提供了一个简单的方法来处理WebSocket连接和消息。
# flask_sock更加轻量级，如果你只需要基本的WebSocket功能，而不需要Socket.IO的额外特性，那么flask_sock可能是一个更好的选择。
# 它适合那些需要快速实现简单WebSocket服务的场景，而不需要Socket.IO的额外开销。

from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        print("<<<", data)

        sock.send(data)
        print(">>>", data)

if __name__ == '__main__':
    app.run(port=1234)