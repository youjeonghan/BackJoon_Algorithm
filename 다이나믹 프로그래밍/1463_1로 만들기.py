
# 초기 접근 첫번째로 시도했던 코드 (탑다운방식)
# import math,sys
# sys.setrecursionlimit(200000)
#
# x = int(input())
# cnt = 0
# array=[0 for i in range(int(math.pow(10,6))+1)]
# def dynamic(x, cnt, array):
#     if x%3 == 0:
#         if array[int(x / 3)] > cnt+1 or array[int(x / 3)] ==0:
#             array[int(x / 3)] = cnt+1
#             dynamic(x/3, cnt+1, array)
#
#     if x%2 == 0:
#         if array[int(x / 2)] > cnt+1 or array[int(x / 2)] ==0:
#             array[int(x / 2)] = cnt+1
#             dynamic(x / 2, cnt + 1, array)
#     if x - 1 > 1:
#         if array[int(x - 1)] > cnt + 1 or array[int(x - 1)] ==0:
#             array[int(x - 1)] = cnt + 1
#             dynamic(x - 1, cnt + 1, array)
#
# dynamic(x, cnt, array)
# print(array[1])
import math

x = int(input())
n=1
cnt = 0
array=[0 for i in range(int(math.pow(10,6))+1)]
def dynamic(x, cnt, array):
    if x%3 == 0:
        if array[int(x / 3)] > cnt+1 or array[int(x / 3)] ==0:
            array[int(x / 3)] = cnt+1
            dynamic(x/3, cnt+1, array)

    if x%2 == 0:
        if array[int(x / 2)] > cnt+1 or array[int(x / 2)] ==0:
            array[int(x / 2)] = cnt+1
            dynamic(x / 2, cnt + 1, array)
    if x - 1 > 1:
        if array[int(x - 1)] > cnt + 1 or array[int(x - 1)] ==0:
            array[int(x - 1)] = cnt + 1
            dynamic(x - 1, cnt + 1, array)

while n>

dynamic(x, cnt, array)
print(array[1])
