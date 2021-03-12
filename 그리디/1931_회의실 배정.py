# 실버 2레벨    회의실 배정
from sys import stdin

N = int(stdin.readline().strip())
li = []
for i in range(N):
    a, b = map(int, stdin.readline().strip().split())
    li.append((a, b))

li.sort(key=lambda x: (x[1], x[0]))
# print(li)
result = []
idx = 0
point = li[0]

for i in range(1, N):
    if li[i][1] < point[1]:
        point = li[i]

    if point[1] <= li[i][0]:
        result.append(point)
        point = li[i]

result.append(point)
print(len(result))