import time
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            time.sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi!")
            time.sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
t2.start()
