# 골드 5레벨
# 20분 소요
# bfs

from collections import deque

n, k = map(int, input().split())
arr = [float("inf")] * 100001
stack = deque([(n, 0)])

answer = [-1, 0]
while stack:
    num, idx = stack.popleft()
    if arr[num] < idx:
        continue
    arr[num] = idx
    if num == k and (answer[0] == -1 or idx == answer[0]):
        answer[0] = idx
        answer[1] += 1
        continue

    if num + 1 <= 100000:
        stack.append((num + 1, idx + 1))
    if num * 2 <= 100000:
        stack.append((num * 2, idx + 1))
    if num - 1 >= 0:
        stack.append((num - 1, idx + 1))

print(answer[0])
print(answer[1])