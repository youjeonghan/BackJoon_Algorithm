# 실버 1레벨
# 다시 풀기


n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]

li.sort()
arr = [float("inf")] * (k + 1)
arr[0] = 0

for i in li:
    for j in range(i, k + 1):
        arr[j] = min(arr[j], arr[j - i] + 1)


print(arr[k] if arr[k] != float("inf") else -1)
