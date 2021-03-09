# 실버 2레벨        가장 긴 증가하는 부분 수열
from sys import stdin

read = stdin.readline

N = int(read())
seq = list(map(int, read().split()))
li = []
dic = {}
result = 0

for i in seq:
    _max = 0

    for j in li:
        if j < i and dic.get(j) > _max:
            _max = dic.get(j)

    li.append(i)

    dic[i] = _max + 1
    if result < dic[i]:
        result = dic[i]

print(result)