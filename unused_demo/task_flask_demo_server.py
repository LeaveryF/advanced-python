# 要求每秒钟服务器回响应的话 http不适用的?



from flask import Flask, request, jsonify
import threading
import time
import queue

app = Flask(__name__)

# 创建优先队列
priority_queue = queue.PriorityQueue()
# 存储已处理的请求
processed_requests = []

# 处理优先队列中最高优先级请求的函数
def process_queue():
    while True:
        if not priority_queue.empty():
            priority, number = priority_queue.get()
            processed_requests.append(number)
            # 处理请求，这里简单模拟处理
            print(f"Processed: {number}")
        time.sleep(1)  # 每秒处理一次

# 启动处理线程
# daemon表示设置为守护线程
threading.Thread(target=process_queue, daemon=True).start()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    if 'number' not in data:
        return jsonify({"error": "Invalid input"}), 400

    number = data['number']
    # priority = data.get('priority', number)
    priority = number  # 默认优先级为数值本身
    priority_queue.put((priority, number))

    return jsonify({"message": "Number added to the queue"}), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "queue_length": priority_queue.qsize(),
        "processed_requests": processed_requests
    }), 200

if __name__ == '__main__':
    app.run(debug=True)