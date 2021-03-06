# 실버 3레벨        스택 수열
from sys import stdin

stack = []
result = []
goal = []
n = int(stdin.readline())
for _ in range(n):
    goal.append(int(stdin.readline()))

idx = 0
for i in range(1, n + 1):
    stack.append(i)
    result.append("+")
    while idx != len(goal) and stack and stack[-1] == goal[idx]:
        stack.pop()
        result.append("-")
        idx += 1

if stack:
    print("NO")
else:
    print("\n".join(result))
