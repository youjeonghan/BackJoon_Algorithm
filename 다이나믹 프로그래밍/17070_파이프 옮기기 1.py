# 골드 5레벨

n = int(input())
possible = []
for _ in range(n):
    possible.append(list(map(int, input().split())))


gp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(3)]
gp[2][1][2] = 1
for y in range(1, n + 1):
    for x in range(1, n + 1):
        if possible[y - 1][x - 1] == 1:
            continue
        check = [possible[y - 2][x - 1], possible[y - 2][x - 2], possible[y - 1][x - 2]]
        num = 0
        num += gp[0][y - 1][x] + gp[1][y - 1][x]
        gp[0][y][x] += num

        num = 0
        if check[0] == check[2] == 0:
            num += gp[0][y - 1][x - 1] + gp[1][y - 1][x - 1] + gp[2][y - 1][x - 1]
        gp[1][y][x] += num

        num = 0
        num += gp[1][y][x - 1] + gp[2][y][x - 1]
        gp[2][y][x] += num

print(gp[0][n][n] + gp[1][n][n] + gp[2][n][n])