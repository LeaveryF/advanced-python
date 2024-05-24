import asyncio
from flask import Flask
from flask_sock import Sock
from queue import PriorityQueue

app = Flask(__name__)
sock = Sock(app)

priority_queue = PriorityQueue()

async def send_data():
    while True:
        if not priority_queue.empty():
            num = priority_queue.get()
        else:
            num = "None"
        message = f"<{num}, {priority_queue.qsize()}>"

        await sock.send(message)
        print(">>>", message)
        await asyncio.sleep(1)

@sock.route('/echo')
async def echo(sock):
    asyncio.create_task(send_data())
    while True:
        data = await sock.receive()
        print("<<<", data)
        priority_queue.put(int(data))
        num = int(data)

if __name__ == '__main__':
    app.run(host="localhost", port=1234)
