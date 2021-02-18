# 브론즈 1레벨      이항 계수 1
from itertools import combinations

N, K = map(int, input().split())
print(len(list(combinations(N * [0], K))))
