#!/usr/bin/env python35

""" results:
1686371 th fib
time: 60.00003218650818

41369542 th fib % 65536 is 59970
time: 60.00000190734863
"""
import time

# M = M %*% [[1, 1], [1, 0]]
# fib(n) is M[0][1]
M = [[1, 1], [1, 0]]
i = 2
t1 = time.time()
while 1:
    i += 1
    a11 = M[0][0] + M[1][0]
    a12 = M[0][1] + M[1][1]
    a21 = M[0][0]
    a22 = M[0][1]
    M = [[a11, a12], [a21, a22]]
    t2 = time.time()
    # print(i, M[0][1])
    if t2-t1 > 60:
        break
print(i, "th fib")
print("time:", t2-t1)


# modulo part
M_m = [[1, 1], [1, 0]]
i = 2
t3 = time.time()
# we only need to modulo a11 and a12
while 1:
    i += 1
    a11 = (M_m[0][0] + M_m[1][0]) % 65536
    a12 = (M_m[0][1] + M_m[1][1]) % 65536
    a21 = M_m[0][0]
    a22 = M_m[0][1]
    M_m = [[a11, a12], [a21, a22]]
    t4 = time.time()
    # print(i, M_m)
    if t4-t3 > 60:
        break
print(i, "th fib % 65536 is", M_m[0][1])
print("time:", t4-t3)


