# 골드 5레벨

n = int(input())
arr = [i for i in range(101)]

for i in range(2, n + 1):
    temp = arr[i]
    for j in range(i + 3, n + 1):
        temp += arr[i]
        if arr[j] < temp:
            arr[j] = temp

print(arr[n])