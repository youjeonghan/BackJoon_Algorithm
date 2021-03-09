# 실버 2레벨        스티커
from sys import stdin

read = stdin.readline

T = int(read())
for _ in range(T):
    n = int(read())
    li = []
    _max = []
    for _ in range(2):
        li.append(list(map(int, read().split())))
        _max.append([0] * n)
    _max[0][0] = li[0][0]
    _max[1][0] = li[1][0]
    _max[0][1] = _max[1][0] + li[0][1]
    _max[1][1] = _max[0][0] + li[1][1]
    for i in range(2, n):
        _max[0][i] = max(_max[1][i - 1] + li[0][i], _max[1][i - 2] + li[0][i])
        _max[1][i] = max(_max[0][i - 1] + li[1][i], _max[0][i - 2] + li[1][i])

    print(max(_max[0][n - 1], _max[1][n - 1]))
