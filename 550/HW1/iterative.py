#!/usr/bin/env python35

""" results:
801079 th fib
time 60.00001502037048

132462546 th fib % 65536 is 6589
time 60.000000953674316
"""
import time


# def fib(n):
#     A = [0, 1]
#     for i in range(n):
#         A.append(A[-1] + A[-2])
#     return A[n]


def fib():
    A = [0, 1]
    t1 = time.time()
    while 1:
        yield A.append(A[-1] + A[-2])
        t2 = time.time()
        if t2 - t1 > 60:
            break
    print(len(A), "th fib")
    print("time", t2-t1)

list(fib())


# modulo part
def fib_m():
    A = [0, 1]
    t3 = time.time()
    while 1:
        yield A.append((A[-1]+A[-2]) % 65536)
        t4 = time.time()
        if t4 - t3 > 60:
            break
    print(len(A), "th fib % 65536 is", A[-1])
    print("time", t4-t3)

list(fib_m())
