# 通过继承Thread类实现多线程



import threading

# 另一种方法 继承Thread类 即创建Thread的子类 这种方法更灵活
class MyThread(threading.Thread):
    # 重新实现__init__方法 注意此时必须调用父类的__init__
    def __init__(self, name):
        super().__init__()
        self.name = name

    # 必须重写run函数 且run函数不允许在外部人为调用
    def run(self):
        print("Thread {} is running.".format(self.name))

# 创建多个线程并启动它们
threads = []
for i in range(5):
    thread = MyThread(name=f"Thread-{i}") # 其实你不指定name它会自动生成个类似的name
    threads.append(thread)
    # 启动线程 自动执行run函数
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()
