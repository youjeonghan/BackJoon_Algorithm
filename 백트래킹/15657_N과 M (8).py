# 실버 3레벨        N과 M (8)
from sys import stdin

read = stdin.readline

n, m = map(int, read().split())
li = list(map(int, read().split()))
li.sort()


def back(result, s):
    if len(result) == m:
        return print(" ".join(map(str, result)))

    for i in range(s, len(li)):
        result.append(li[i])
        back(result, i)
        result.pop()


back([], 0)
