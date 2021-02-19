# 실버 5레벨    좌표 정렬하기
from sys import stdin

N = int(input())

li = []
for _ in range(N):
    li.append(list(map(int, stdin.readline().split())))

li.sort(key=lambda x: (x[0], x[1]))

for i in li:
    print(i[0], i[1])
