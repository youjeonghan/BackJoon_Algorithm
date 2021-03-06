# 실버 3레벨        랜선 자르기
# 다시
from sys import stdin

K, N = map(int, stdin.readline().split())
li = []
for _ in range(K):
    li.append(int(stdin.readline()))
_min = 1
_max = max(li)
_mid = (_min + _max) // 2
while _min <= _max:
    _mid = (_min + _max) // 2
    cnt = 0
    for i in li:
        cnt += i // _mid

    if cnt >= N:
        _min = _mid + 1

    else:
        _max = _mid - 1

print(_max)

# 처음 시도한 시간초과 코드
# from sys import stdin

# K, N = map(int, stdin.readline().split())
# li = []
# for _ in range(K):
#     li.append(int(stdin.readline()))

# t = int(sum(li) / N)

# while t:
#     cnt = 0
#     for i in li:
#         cnt += i // t

#     if cnt >= N:
#         print(t)
#         break

#     else:
#         t -= 1
