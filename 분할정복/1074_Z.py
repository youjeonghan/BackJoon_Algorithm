# 실버 1레벨    Z

t = 0


def divide(l, x, y, start):
    l = int(l // 2)
    if l == 1:
        if x == 0 and y == 0:
            print(start)

        if x == 0 and y == 1:
            print(start + 1)

        if x == 1 and y == 0:
            print(start + 2)

        if x == 1 and y == 1:
            print(start + 3)

    elif x < l and y < l:
        divide(l, x, y, start + 0)

    elif x < l and y >= l:
        divide(l, x, y - l, start + l * l * 1)

    elif x >= l and y < l:
        divide(l, x - l, y, start + l * l * 2)

    else:
        divide(l, x - l, y - l, start + l * l * 3)


N, r, c = map(int, input().split())

divide(2 ** N, r, c, 0)