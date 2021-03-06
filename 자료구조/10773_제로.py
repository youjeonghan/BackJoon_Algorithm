# 실버 4레벨        제로
from sys import stdin

stack = []
K = int(stdin.readline())

for _ in range(K):
    x = int(stdin.readline())
    if x != 0:
        stack.append(x)
    else:
        stack.pop()

print(sum(stack))