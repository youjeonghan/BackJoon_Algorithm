# 실버 4레벨    비밀번호 찾기

from sys import stdin

read = stdin.readline
N, M = map(int, read().split())

dic = {}

for _ in range(N):
    site, id = read().rstrip().split()
    dic[site] = id

for _ in range(M):
    site = read().rstrip()
    print(dic[site])