### kmp 알고리즘

target = "ababacabacaabacaaba"
pattern = "abacaaba"
table = [0] * len(pattern)


def make_table(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:  # 안맞으면 맞는부분까지 j내리기
            j = table[j - 1]
        if pattern[j] == pattern[i]:
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
                print(f"{i-len(pattern)+2}번째 일치")
                j = table[j]
            else:
                j += 1


kmp(target, pattern)
# ------------------------------------------------------------------------------------------------------------