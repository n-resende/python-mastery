import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def parse_line(line: str):
    split = line.split(sep='=')
    name = split[0]
    value = split[1]
    return (name,value)

def worker(x, y):
    print('About to work')
    time.sleep(5)
    print('Done')
    return x + y

def do_work(x, y, fut):
    fut.set_result(worker(x,y))

print(parse_line('email=guido@python.org'))

fut = Future()
t = threading.Thread(target=do_work, args=(1,2, fut))
t.start()
print(fut.result())

pool = ThreadPoolExecutor()
fut = pool.submit(worker, 1, 2)
print(fut.result())