# 골드 5레벨        숨바꼭질 3
# 39분 소요


import heapq as hq

n, k = map(int, input().split())
arr = [1 for _ in range(100001)]
arr[n] = 0  # 들렸다
heap = [(0, n)]


def bfs():
    while heap:
        time, v = hq.heappop(heap)

        if v == k:
            print(time)
            return

        if v * 2 <= 100000 and arr[v * 2]:
            arr[v * 2] = 0
            hq.heappush(heap, (time, v * 2))
        if 0 <= v - 1 and arr[v - 1]:
            arr[v - 1] = 0
            hq.heappush(heap, (time + 1, v - 1))
        if v + 1 <= 100000 and arr[v + 1]:
            arr[v + 1] = 0
            hq.heappush(heap, (time + 1, v + 1))


bfs()