# update_1:
# 服务器无数据时不进行发送
# 队列为空时 PriorityQueue.get自动阻塞(挂起)
# 由于需求的原因 不太好测试 因为这样实际上需要指定客户端的优先级

# 这意味着 当队列为空时 任何新到达的请求都能被立刻处理

# 功能：
# 运行python脚本在本地ws://loaclhost:1234建立一个服务器
# 客户端访问ws://loaclhost:1234/echo将与服务器建立websocket连接
# 建立连接后 客户端可以在任何时候向服务器发送单个整数的数据
# 服务器端维护一个优先队列 每接收到客户端发送的数据后 立刻加入优先队列
# 建立连接后 对于每个客户端 服务器每隔1秒钟发送 "<最大数字, 优先队列长度>" 给客户端
# 使用多线程实现 使用python的queue模块保证线程安全 支持多客户端
# 经测试多客户端是没问题的

# 测试方法：
# 在apifox中 - 新建websocket接口 - 地址填写ws://localhost:1234/echo
#           - 点击连接 - 显示连接成功后,会每隔1秒接收到服务器的数据
#           - 输入请求(一个数字) - 点击发送即向服务器发送该数据
# 测试多客户端就在apifox中创建多个websocket接口

from flask import Flask
from flask_sock import Sock
from queue import PriorityQueue
from threading import Thread
from simple_websocket import ConnectionClosed

app = Flask(__name__)
sock = Sock(app)

# Python的queue模块通过使用锁机制来实现线程安全
# 意思就是在队列上使用多线程不需要手动加锁 python的queue的内部帮你实现了
# queue模块提供了几种队列类，如Queue、LifoQueue和PriorityQueue，它们都是线程安全的
# 因此 虽然python有锁 但简单的多线程程序尽量使用queue模块内部封装的锁 以降低编程的复杂性
# 当然 queue模块为保证线程安全 代价是牺牲了效率
# 所以 即使有多个客户端 也不会影响该程序的正确性
priority_queue = PriorityQueue()

# 发送线程 用于服务器每隔1秒发送数据给客户端
# python的多线程有两种写法 一种是直接创建
# 另一种是继承Thread类 即创建Thread的子类 这种方法更灵活
# 需要重新实现__init__方法 必须调用父类的__init__
# 必须重写run函数 且run函数不允许在外部人为调用
class SendThread(Thread):
    def __init__(self, ws):
        super().__init__()
        self.ws = ws
    
    def run(self):
        try:
            while True:
                # 从优先队列中获取数据
                # 如果优先队列为空 线程自动阻塞(挂起)
                num = -priority_queue.get()
                message = f"<{num}, {priority_queue.qsize()}>"

                # websocket发送的数据是字符串的数据 即使是json数据 至少这里是
                self.ws.send(message)
                print(">>>", message)

        # 捕获连接中断的异常
        except ConnectionClosed as err:
            pass

# 接收一个websocket参数 表示该websocket连接
# 参考网站：
# https://flask-sock.readthedocs.io/en/latest/index.html
# https://flask-sock.readthedocs.io/en/latest/quickstart.html#example
# 没有使用异步函数 因为太难用不知道为什么总是出问题
# 网络并不繁忙时 receive和send并不会占用太多时间所以影响并不大
@sock.route('/echo')
def echo(ws):
    # 创建并启动线程
    # 需要传递ws参数 lock锁参数
    send_thread = SendThread(ws)
    send_thread.start()

    try:
        while True:
            data = ws.receive()
            num = int(data)
            print("<<<", num)
            priority_queue.put(-num) # 通过取相反数实现大根堆

    # 捕获连接中断的异常
    except ConnectionClosed as err:
        print(f"A client has disconnected: {err}")

if __name__ == '__main__':
    app.run(host="localhost", port=1234)
