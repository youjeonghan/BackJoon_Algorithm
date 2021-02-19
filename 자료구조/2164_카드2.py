# 실버 4레벨    카드2
from collections import deque

N = int(input())

li = deque([i for i in range(1, N + 1)])
while len(li) != 1:
    li.popleft()
    li.append(li.popleft())

print(li[0])
