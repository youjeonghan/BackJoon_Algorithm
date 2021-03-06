# 실버 5레벨        좌표 정렬하기 2
from sys import stdin

N = int(stdin.readline())
li = []
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    li.append((x, y))

li.sort(key=lambda x: (x[1], x[0]))
for i in li:
    print(i[0], i[1])
