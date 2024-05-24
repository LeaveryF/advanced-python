# python多线程的锁



import threading

# 共享资源
shared_resource = 0

# 锁对象
lock = threading.Lock()

def increment():
    global shared_resource
    # 修改共享资源
    for _ in range(100):
        # 获取锁
        lock.acquire()
        shared_resource += 1
        print(threading.current_thread().name + ':', shared_resource)
        # 释放锁
        lock.release()

# 创建多个线程并启动它们
threads = []
for i in range(10):
    thread = threading.Thread(target=increment, name = f"Thread-{i}")
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print("Shared resource value:", shared_resource)
