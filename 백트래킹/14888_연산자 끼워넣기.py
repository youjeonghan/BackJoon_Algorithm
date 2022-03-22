# 실버 1레벨
# 백트래킹
# 20분 소요

_ = input()
num = list(map(int, input().split()))
cal = list(map(int, input().split()))
min_answer = float("inf")
max_answer = -float("inf")


def calculation(arr):
    global min_answer, max_answer
    acc = num[0]
    for i in range(len(arr)):
        if arr[i] == "+":
            acc += num[i + 1]
        elif arr[i] == "-":
            acc -= num[i + 1]
        elif arr[i] == "*":
            acc *= num[i + 1]
        elif arr[i] == "/":
            if acc < 0 and num[i + 1] > 0:
                acc = -(abs(acc) // num[i + 1])
            else:
                acc //= num[i + 1]
    min_answer = min(min_answer, acc)
    max_answer = max(max_answer, acc)


def add_sign(arr, sign):
    arr.append(sign)
    track(arr)
    arr.pop()


def track(arr):
    if len(arr) == len(num) - 1:
        calculation(arr)
        return
    if cal[0] > 0:
        cal[0] -= 1
        add_sign(arr, "+")
        cal[0] += 1
    if cal[1] > 0:
        cal[1] -= 1
        add_sign(arr, "-")
        cal[1] += 1
    if cal[2] > 0:
        cal[2] -= 1
        add_sign(arr, "*")
        cal[2] += 1
    if cal[3] > 0:
        cal[3] -= 1
        add_sign(arr, "/")
        cal[3] += 1


track([])
print(max_answer)
print(min_answer)