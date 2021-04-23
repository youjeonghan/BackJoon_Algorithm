# 골드 4레벨    부분합
from sys import stdin

read = stdin.readline
N, S = map(int, read().split())
li = list(map(int, read().split()))
s = 0
e = -1

_len = float("inf")
sum = 0
while 1:
    if (sum < S and e == len(li) - 1) or (s == len(li)):
        break

    if sum < S:
        e += 1
        sum += li[e]
    else:
        if e >= s and _len > e - s + 1:
            _len = e - s + 1
        sum -= li[s]
        s += 1

_len = 0 if _len == float("inf") else _len
print(_len)
