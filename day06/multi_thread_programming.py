import multiprocessing


def proc1():
    return 9999899**9999


def proc2():
    return 888888**8888


p1  = multiprocessing.Process(target = proc1)
p2  = multiprocessing.Process(target = proc2)


p1.start()
p2.start()


p1.join()
p2.join()
