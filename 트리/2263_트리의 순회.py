# 골드 3레벨        트리의 순회
# 다시


# 내 코드 아님 공부 할때 봤던 코드
# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 9)


# def divide(root, left, right, plus):
#     if left > right or right < left:
#         return
#     print(root, end=" ")
#     temp = num[root]
#     L = temp - left
#     R = right - temp
#     if plus + L - 1 < n:
#         divide(post_order[plus + L - 1], left, temp - 1, plus)
#     if plus + L + R - 1 < n:
#         divide(post_order[plus + L + R - 1], temp + 1, right, plus + L)


# n = int(input())
# in_order = list(map(int, input().split()))
# post_order = list(map(int, input().split()))
# num = [0] * (n + 1)
# for i in range(n):
#     num[in_order[i]] = i
# root = post_order[-1]
# divide(root, 0, n - 1, 0)
