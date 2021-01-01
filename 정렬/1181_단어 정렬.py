# 1181_단어 정렬
import sys

cnt = int(input())

list_ch = []
for i in range(cnt):
    st = sys.stdin.readline().rstrip()
    list_ch.append(st)

set_ch = set(list_ch)
list_ch = list(set_ch)
list_ch.sort()

for i in range(51):
    for j in list_ch:
        if len(j) == i:
            print(j)