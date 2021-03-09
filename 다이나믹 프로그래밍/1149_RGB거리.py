# 실버 1레벨        RGB거리
from sys import stdin, maxsize

read = stdin.readline
N = int(read())
_min = [[maxsize, maxsize, maxsize] for _ in range(N + 1)]
r = []
g = []
b = []
for _ in range(N):
    command = list(map(int, read().split()))
    r.append(command[0])
    g.append(command[1])
    b.append(command[2])

_min[0] = [r[0], g[0], b[0]]
for i in range(1, N):
    _min[i][0] = r[i]
    _min[i][0] += _min[i - 1][1] if _min[i - 1][1] < _min[i - 1][2] else _min[i - 1][2]

    _min[i][1] = g[i]
    _min[i][1] += _min[i - 1][0] if _min[i - 1][0] < _min[i - 1][2] else _min[i - 1][2]

    _min[i][2] = b[i]
    _min[i][2] += _min[i - 1][1] if _min[i - 1][1] < _min[i - 1][0] else _min[i - 1][0]

print(min(_min[N - 1]))
