# 9012_괄호

cmd = int(input())
open_cnt = 0
close_cnt = 0

for i in range(0,cmd):
    arr = list(input())
    for j in range(0,len(arr)):
        if arr[j] == "(":
            open_cnt += 1
        if arr[j] == ")":
            close_cnt += 1

        if close_cnt > open_cnt:
            break
    if close_cnt == open_cnt:
        print("YES")
    else:
        print("NO")
    open_cnt = 0
    close_cnt = 0