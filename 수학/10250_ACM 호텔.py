# 브론즈 3레벨      ACM 호텔

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    room = ((N - 1) // H) + 1
    floor = N % H if N % H != 0 else H
    print(floor * 100 + room)
