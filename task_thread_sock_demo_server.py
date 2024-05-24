from flask import Flask
from flask_sock import Sock
from queue import PriorityQueue
from threading import Thread
from simple_websocket import ConnectionClosed

import time

app = Flask(__name__)
sock = Sock(app)

priority_queue = PriorityQueue()

class SendThread(Thread):
    def __init__(self, ws):
        super().__init__()
        self.ws = ws
    
    def run(self):
        try:
            while True:
                if not priority_queue.empty():
                    num = -priority_queue.get()
                else:
                    num = "None"
                message = f"<{num}, {priority_queue.qsize()}>"

                self.ws.send(message)
                print(">>>", message)
                time.sleep(1)

        except ConnectionClosed as err:
            pass

@sock.route('/echo')
def echo(ws):
    send_thread = SendThread(ws)
    send_thread.start()

    try:
        while True:
            data = ws.receive()
            print("<<<", data)
            priority_queue.put(-int(data))
            num = int(data)

    except ConnectionClosed as err:
        print(f"A client has disconnected: {err}")

if __name__ == '__main__':
    app.run(host="localhost", port=1234)
