# 골드 4레벨

from itertools import combinations

n, k = map(int, input().split())
arr = []
union = set()
for _ in range(n):
    arr.append(set(input()))
    union = union | arr[-1]

union = list(union)

sign = []
answer = 0


def tracking(idx):
    if idx >= len(union):
        return
    if len(sign) == k:
        check(sign)
        return

    sign.append(union[idx])
    idx += 1
    tracking(idx)
    sign.pop()
    tracking(idx)


def check(sign):
    global answer
    temp = set(sign)
    cnt = 0
    for i in arr:
        if len(i - temp) == 0:
            cnt += 1
    answer = max(answer, cnt)


tracking(0)
print(answer)