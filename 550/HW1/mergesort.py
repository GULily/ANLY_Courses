#!/usr/bin/env python35

"""
test code:
 $ echo 11,77,2,9,6,3,4,7 | python mergesort.py
"""

import sys


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

if __name__ == '__main__':
    input_list = sys.stdin.read()
    data = list(map(int, input_list.split(',')))
    print(mergesort(data))

