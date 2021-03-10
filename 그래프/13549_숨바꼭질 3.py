# 골드 5레벨        숨바꼭질 3
# 다시
from collections import deque
from sys import stdin

read = stdin.readline
N, K = map(int, read().split())
li = [-1] * 200001


def check(start, time):
    _set = set()
    # print(start)
    for i in start:
        while i != 0 and i <= 200000:
            # print(i)
            if li[i] == -1:
                li[i] = time
                _set.add(i)

            if i > K:
                break
            i *= 2

    return _set


def plus(start, time):
    _set = check(start, time)
    if li[K] != -1:
        return
    time += 1
    start = []
    for i in _set:
        if i - 1 > 0 and li[i - 1] == -1:
            li[i - 1] = time
            start.append(i - 1)

        if li[i + 1] == -1:
            li[i + 1] = time
            start.append(i + 1)

        if li[K] != -1:
            return
    if start:
        plus(start, time)


plus([N], 0)
# print(li[1:18])
print(li[K])