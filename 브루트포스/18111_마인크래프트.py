# 실버 3레벨        마인크래프트
# 다시
from sys import stdin, maxsize
from collections import Counter

N, M, B = map(int, stdin.readline().split())
li = []
for _ in range(N):
    li.append(list(map(int, stdin.readline().split())))

li = sum(li, [])
count = Counter(li)
li = list(count.items())
li.sort(reverse=True)
result = (maxsize, 0)
for i in range(0, 257):
    flag, time = 1, 0
    inven = B
    for j in li:
        if j[0] >= i:
            time += 2 * (j[0] - i) * j[1]
            inven += (j[0] - i) * j[1]

        elif (i - j[0]) * j[1] <= inven:
            inven -= (i - j[0]) * j[1]
            time += 1 * (i - j[0]) * j[1]

        else:
            flag = 0
            break

    if flag == 1 and result[0] >= time:
        result = (time, i)

print(result[0], result[1])


######## pypy3에서 904ms 나온풀이
# from sys import stdin, maxsize

# N, M, B = map(int, stdin.readline().split())
# li = []
# for _ in range(N):
#     li.append(list(map(int, stdin.readline().split())))
# li = sum(li, [])
# li.sort(reverse=True)
# s = li[-1]
# e = li[0]
# result = (maxsize, 0)
# for i in range(s, e + 1):
#     flag, time = 1, 0
#     inven = B
#     for j in li:
#         if j >= i:
#             time += 2 * (j - i)
#             inven += j - i

#         elif i - j <= inven:
#             inven -= i - j
#             time += 1 * (i - j)

#         elif i - j > inven or time > result[0]:
#             flag = 0
#             break

#     if flag == 1 and result[0] > time:
#         result = (time, i)

#     elif flag == 1 and result[0] == time and result[1] < i:
#         result = (time, i)

# print(result[0], result[1])
