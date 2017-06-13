#!/usr/bin/env python35

""" results:
39 th fib is: 63245986
time: 37.16418218612671
40 th fib is: 102334155
time: 60.68246603012085

39 th fib % 65536 is 3746
time: 38.5799617767334
40 th fib % 65536 is 32459
time: 62.39828896522522

"""

import time


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# test the calculation time from fib(39) to fib(40)
for n in range(39, 41):
    t1 = time.time()
    fib1 = fib(n)
    t2 = time.time()
    print(n, "th fib is:", fib1)
    print("time:", t2 - t1)


# modulo part
def fib_m(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib_m(n - 1) + fib_m(n - 2)) % 65536

# test the calculation time from fib(39) to fib(40)
for n in range(39, 41):
    t3 = time.time()
    fib2 = fib_m(n)
    t4 = time.time()
    print(n, "th fib % 65536 is", fib2)
    print("time:", t4 - t3)


