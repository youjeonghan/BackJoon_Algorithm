# 1920_수 찾기

N = int(input())

list1 = sorted(input().split())


M = int(input())

list2 = input().split()

# 시간 초과
# for num in list2:
#     if num in list1:
#         print(1)
#     else:
#         print(0)

# 이진탐색
for target in list2:
    l = 0
    r = len(list1) - 1
    in_check = 0
    while l <= r:
        mid = (l + r) // 2
        if list1[mid] == target:
            in_check = 1
            break

        elif list1[mid] > target:
            r = mid - 1

        else:
            l = mid + 1

    if in_check:
        print(1)
    else:
        print(0)
