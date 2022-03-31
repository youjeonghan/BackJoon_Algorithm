# 실버 1레벨
# 구글링 일반 풀이와 다름

from sys import stdin
from collections import defaultdict
import heapq as hq

read = stdin.readline

n = int(read())
arr = [[0, 0]]
for _ in range(n):
    t, p = map(int, read().split())
    arr.append([t, p])


dic = defaultdict(list)
for i in range(1, n + 1):
    t, p = arr[i]
    hq.heappush(dic[i + t - 1], -(arr[i - 1][1] + p))

    if dic[i]:
        p = hq.heappop(dic[i])
        p = -p
        arr[i][1] = max(p, arr[i - 1][1])
    else:
        arr[i][1] = arr[i - 1][1]

print(arr[-1][1])