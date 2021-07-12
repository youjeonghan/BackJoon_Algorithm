# 실버 2레벨    종이의 개수
# 코드 업그레이드 가능
# 다시

from sys import stdin
from collections import defaultdict

read = stdin.readline
N = int(read())
li = []
result = defaultdict(int)
for _ in range(N):
    li.append(list(map(int, read().split())))


def div(start, edge):
    if edge == 1:
        result[li[start[0]][start[1]]] += 1
        return 0

    cnt = defaultdict(int)
    for dy in range(edge):
        for dx in range(edge):
            cnt[li[start[0] + dy][start[1] + dx]] += 1
            count = 0
            for i in range(-1, 2):
                if cnt[i] == 0:
                    count += 1
            if count <= 1:
                break

    if cnt[-1] == edge ** 2:
        result[-1] += 1
    elif cnt[0] == edge ** 2:
        result[0] += 1
    elif cnt[1] == edge ** 2:
        result[1] += 1
    else:
        for dy in range(0, edge, edge // 3):
            for dx in range(0, edge, edge // 3):
                div((start[0] + dy, start[1] + dx), edge // 3)


div((0, 0), N)
print(result[-1])
print(result[0])
print(result[1])