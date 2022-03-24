# 골드 4레벨
# 복습

from sys import stdin

read = stdin.readline

v, e = map(int, read().split())

info = []
for _ in range(e):
    info.append(list(map(int, read().split())))

info.sort(key=lambda x: x[2])
check = [i for i in range(v + 1)]


def union(n1, n2):
    union_n1, union_n2 = find(n1), find(n2)
    if union_n1 > union_n2:
        check[union_n1] = union_n2
    else:
        check[union_n2] = union_n1


def find(n):
    if check[n] == n:
        return n
    check[n] = find(check[n])
    return check[n]


answer = 0
for start, end, weight in info:
    if find(start) == find(end):
        continue
    union(start, end)
    answer += weight

print(answer)