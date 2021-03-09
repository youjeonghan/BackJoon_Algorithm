# 실버 1레벨        정수 삼각형
from sys import stdin

read = stdin.readline

n = int(read())
li = [[0]]
_max = [[0]]
for i in range(n):
    li.append(list(map(int, read().split())))
    _max.append([0] * (i + 1))

# _max[0][0] = li[0][0]
for i in range(1, n + 1):
    for idx, j in enumerate(li[i]):
        if idx == 0:
            _max[i][idx] = _max[i - 1][idx] + j
        elif idx == len(li[i]) - 1:
            _max[i][idx] = _max[i - 1][idx - 1] + j
        else:
            _max[i][idx] = (
                _max[i - 1][idx - 1] + j
                if _max[i - 1][idx - 1] > _max[i - 1][idx]
                else _max[i - 1][idx] + j
            )

print(max(_max[n]))
