import threading

g_count = 0

def thread_main():
    global g_count
    for i in range(100000):
        g_count += 1

threads = []

for i in range(50):
    th = threading.Thread(target= thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print("g_count : {}".format(g_count))