# 골드 3레벨
# kmp 알고리즘
# 다시 풀기


p = input()
s = input()

table = [0] * len(s)


def make_table(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and s[j] != s[i]:  # 안맞으면 맞는부분까지 j내리기
            j = table[j - 1]
        if s[j] == s[i]:
            j += 1
            table[i] = j  # i번째 문자열 까지 j개만큼 접두사, 접미사 일치 (0부터 i번째)


def kmp(target, pattern):
    j = 0
    make_table(pattern)
    for i in range(len(target)):
        while j > 0 and pattern[j] != target[i]:
            j = table[j - 1]
        if pattern[j] == target[i]:
            if j == len(pattern) - 1:
                return 1
            j += 1
    return 0


print(kmp(p, s))
