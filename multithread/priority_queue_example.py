# python的队列模块queue.Queue和优先队列queue.PriorityQueue 自带线程锁



# python是如何实现队列的？
# python有queue模块 deque模块
# 竞赛建议只用deque 单线程下 deque比queue快得多
# 同样的原因 竞赛写优先队列建议使用heapq 而不是queue.PriorityQueue
# queue模块为保证线程安全 牺牲了效率

# Python的queue模块通过使用锁机制来实现线程安全
# 意思就是在队列上使用多线程不需要手动加锁 python的queue的内部帮你实现了
# queue模块提供了几种队列类，如Queue、LifoQueue和PriorityQueue，它们都是线程安全的

# 因此 虽然python有锁 但简单的多线程程序尽量使用queue模块内部封装的锁 以降低编程的复杂性

# 这个程序可能有点奇怪:)

import threading
import queue

# 创建一个线程安全的队列
q = queue.PriorityQueue()

def worker(q):
    while True:
        item = q.get()
        if item == -1:  # 终止信号
            break
        # 处理队列中的任务
        print(f"Processing item: {item} . By {threading.current_thread().name}.")
        q.task_done()  # 任务完成通知

# 创建工作线程
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
    threads.append(t)

# 向队列中添加任务
for item in range(1000):
    q.put(item)

# 等待所有任务完成
q.join()

# 发送终止信号给工作线程
for i in range(3):
    q.put(-1)
for t in threads:
    t.join()
