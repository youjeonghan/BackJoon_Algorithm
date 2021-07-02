# 실버 3레벨        N과 M (4)
from sys import stdin

read = stdin.readline

n, m = map(int, read().split())


def back(li, s):
    if len(li) == m:
        print(" ".join(map(str, li)))
        return

    for i in range(s, n + 1):
        li.append(i)
        back(li, i)
        li.pop()


back([], 1)
