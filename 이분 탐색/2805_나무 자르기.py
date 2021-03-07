# 실버 3레벨        나무 자르기
from sys import stdin

N, M = map(int, stdin.readline().split())
li = list(map(int, stdin.readline().split()))
li.sort(reverse=True)
s = 1
e = li[0]
while s <= e:
    m = (s + e) // 2
    sum = 0
    for i in li:
        if i > m:
            sum += i - m
            if sum >= M:
                break
        
        else:
            break

    if sum >= M:
        s = m + 1

    else:
        e = m - 1

print(e)
