words1 = ["ad", "ac", "a", "aaa", "g", "f", "d", "aa"]
words2 = ["ad", "ac", "a", "aaa", "g", "f", "d", "aa"]


def temp_function(a):
    return -len(a), a


# 아래의 두 결과는 같다
words1.sort(key=temp_function)

words2.sort(key=lambda x: (-len(x), x))

print(words1)
# words1 결과
# ['aaa', 'aa', 'ac', 'ad', 'a', 'd', 'f', 'g']

# words2 결과
# ['aaa', 'aa', 'ac', 'ad', 'a', 'd', 'f', 'g']

# sorted 에 key 사용법
# sort_word = word.sorted(key=lambda x: (len(x), x))
