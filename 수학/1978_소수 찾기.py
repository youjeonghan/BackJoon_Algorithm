# 실버4레벨 1978_소수 찾기


def prime(max):
    prime_list = [True] * (max + 1)
    prime_list[0] = prime_list[1] = False

    for i in range(2, int(max ** 0.5) + 1):
        if prime_list[i] == True:
            for j in range(i + i, max + 1, i):
                prime_list[j] = False

    return prime_list


n = int(input())
li = list(map(int, input().split()))
prime_list = prime(max(li))
print(sum([1 for i in li if prime_list[i] == True]))
