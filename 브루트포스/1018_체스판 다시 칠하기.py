# 1018_체스판 다시 칠하기
import sys


def main():
    # n, m과 보드를 입력받음
    n, m = map(int, input().split())

    all_line = []
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        all_line.append(list(line))

    min = 50 * 50
    for i in range(n - 7):
        for j in range(m - 7):
            check_value = check(i, j, all_line)
            if check_value < min:
                min = check_value

    print(min)


def check(n, m, array):
    """바꿔야할 최솟값 체크 함수
        n,m은 이차원 배열에서 처음 시작하는 왼쪽 맨위 좌표

    Returns :
        min: 변경횟수
    """
    cnt_B = 0
    cnt_W = 0
    standard = array[n][m]
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if "B" != array[n + i][m + j]:
                    cnt_B += 1
                else:
                    cnt_W += 1
            elif (i + j) % 2 == 1:
                if "B" == array[n + i][m + j]:
                    cnt_B += 1
                else:
                    cnt_W += 1

    return cnt_B if cnt_B < cnt_W else cnt_W


main()