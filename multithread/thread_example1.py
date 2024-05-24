# python多线程的基本使用



import threading

# 定义要在线程中执行的任务
def print_numbers():
    for i in range(10):
        print(f"Number from Thread-1: {i}")

def print_letters():
    for letter in 'abcdefghij':
        print(f"Letter from Thread-2: {letter}")

# 创建线程对象
thread1 = threading.Thread(target=print_numbers, name="Thread-1")
thread2 = threading.Thread(target=print_letters, name="Thread-2")

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

print("All threads have finished execution.")
