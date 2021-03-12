# 실버 5레벨        덩치
from sys import stdin

N = int(input())
li = []
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    li.append([x, y, -1])

for i in range(len(li)):
    rank = 1
    for j in li:
        if li[i] == j:
            continue

        if li[i][0] < j[0] and li[i][1] < j[1]:
            rank += 1

    li[i][2] = rank

for i in li:
    print(i[2], end=" ")
