# 실버 2레벨        IOIOI

from sys import stdin


def check(s, e):
    flag = -1  # -1 이상무    0,1,2... 이상
    for i in range(0, e - s + 1):
        if i % 2 == 0 and S[sdx + i] != "I":
            flag = i
            break
        elif i % 2 == 1 and S[sdx + i] != "O":
            flag = i
            break
    return flag


read = stdin.readline
N = int(read())
M = int(read())
S = read()
sdx = result = 0

while sdx + 2 * N < M:

    c = check(sdx, sdx + 2 * N)
    if c == -1:  # 조건 해당
        result += 1
        sdx = sdx + 2 * N
        while sdx + 2 < M and check(sdx, sdx + 2) == -1:
            result += 1
            sdx += 2
    else:
        sdx += c if c != 0 else 1  # 실패한 인덱스로 이동

print(result)
