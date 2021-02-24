# 실버 3레벨    색종이 만들기
from sys import stdin


def check(li):
    global one, zero
    li_one = sum(li, [])
    num = sum(li_one)
    if num == len(li_one):
        one += 1

    elif num == 0:
        zero += 1

    else:
        for i in split(li):
            check(i)


def split(li):
    side = int(len(li[0]) // 2)
    start = [(0, 0), (side, 0), (0, side), (side, side)]
    result = []

    for p in start:
        result.append([[li[p[0] + i][p[1] + j] for j in range(side)] for i in range(side)])

    return result


N = int(stdin.readline().strip())

zero = 0
one = 0
li = []

for i in range(N):
    li.append([int(i) for i in stdin.readline().strip().split()])
if sum(sum(li, [])) == N ** 2 or sum(sum(li, [])) == 0:
    print(0)
    print(0)

else:
    check(li)

    print(zero)
    print(one)