# 실버 3레벨    바이러스
# DFS 이용
from sys import stdin

C = int(stdin.readline().strip())
N = int(stdin.readline().strip())
com = [[0] * (C + 1) for _ in range(C + 1)]
stack = [1]
result = set()

for i in range(N):
    x, y = map(int, stdin.readline().strip().split())
    com[x][y] = com[y][x] = 1

while stack:
    target = stack.pop()
    for i in range(C + 1):
        if com[target][i] == 1:
            com[target][i] = com[i][target] = 2
            stack.append(i)
    result.add(target)

# print(result)
print(len(result) - 1)
