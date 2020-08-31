n,k = map(int, input().split())
cnt = 0
coin = []

for i in range(0, n):
    coin.append(int(input()))

for i in range(n-1, -1, -1):
    if k == 0:
        break
    cnt = cnt + (k // coin[i])
    k = k % coin[i]

print(cnt)
