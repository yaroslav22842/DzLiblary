import time
from time import sleep
import datetime

def Hello():
    print("Hi")
    sleep(1)
    print("hello")
    sleep(3)
    print("bye")
    sleep(2)
    print("See ya")
    return "ended"

def TimeCounter(func):
    def wrapper(*args):
        unix_time_start = datetime.datetime.now().timestamp()
        func(*args)
        unix_time_end = datetime.datetime.now().timestamp()
        print("Time work:")
        result = round(unix_time_end - unix_time_start)
        print(f"{result} secs")
    return wrapper

Start = TimeCounter(Hello)
Start()