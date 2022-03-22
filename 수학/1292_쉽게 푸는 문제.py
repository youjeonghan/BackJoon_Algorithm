# 실버 5레벨
# 13분 소요

a, b = map(int, input().split())

arr = [0] * 1002


def add_arr():
    cnt = 0
    while 1:
        for i in range(1, 1000 + 1):
            for _ in range(i):
                cnt += 1
                arr[cnt] = arr[cnt - 1] + i
                if cnt > b:
                    return


add_arr()
print(arr[b] - arr[a - 1])
