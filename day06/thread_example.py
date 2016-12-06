#!/usr/bin/python3
# Filename: thread_example.py


from threading import thread


x = 5


def double():
    global x
    x = x*2


def plus_ten():
    global x
    x = x + 10


thread1 = Thread(target = double)
thread2 = Thread(target = plus_ten)
thread1.start()
thread2.strat()
thread1.join()
thread2.join()

print(x)
