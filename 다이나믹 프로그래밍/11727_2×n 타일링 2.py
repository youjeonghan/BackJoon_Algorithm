# 실버 3레벨    2×n 타일링 2

n = int(input())
li = [0] * 1001
li[1] = 1
li[2] = 3

for idx in range(3, n + 1):
    li[idx] = li[idx - 2] * 2 + li[idx - 1]

print(li[n] % 10_007)
