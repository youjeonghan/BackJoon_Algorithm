"""
파이썬 알고리즘 코드
"""

### 2개의 변수에 입력을 빠르게 받아야 하는 경우
import sys

n, m = map(int, sys.stdin.readline().split())
# ------------------------------------------------------------------------------------------------------------


### int형 숫자들을 빠른 속도로 입력받아 list로 만들때
from sys import stdin

read = stdin.readline
li = list(map(int, read().split()))
# ------------------------------------------------------------------------------------------------------------


### 조합 이용
from itertools import combinations

li = [1, 2, 3]
combi = list(combinations(li, 2))  # li 원소들의 2개를 선택한 조합의 경우가 list 안에 tuple 형식으로 저장된다.
# ------------------------------------------------------------------------------------------------------------


### (int or float) max값 사용
import sys

int_max = sys.maxsize
int_max2 = float("inf")
# ------------------------------------------------------------------------------------------------------------


### 절대값 ###
abs_num = abs(-10)
# ------------------------------------------------------------------------------------------------------------


### 리스트 뒤집기
li = [1, 2, 3, 4, 5]
print(li[::-1])
# ------------------------------------------------------------------------------------------------------------


### 딕셔너리를 key, value를 기준으로 내림차순 정렬하기
## _dict = dict(sorted(~~~)) 을 하면 다시 딕셔너리가 된다
# key 기준
_dict = {"a": 1, "n": 12, "b": 5, "c": 3, "z": 2}
print(
    sorted(_dict.items(), key=lambda x: x[0], reverse=True)
)  # [('z', 2), ('n', 12), ('c', 3), ('b', 5), ('a', 1)]

# value 기준
print(
    sorted(_dict.items(), key=lambda x: x[1], reverse=True)
)  # [('a', 1), ('z', 2), ('c', 3), ('b', 5), ('n', 12)]
# ------------------------------------------------------------------------------------------------------------


### 딕셔너리의 key, value 값 서로 바꾸기
di = {"a": 0, "b": 1, "c": 2}
di = {v: k for k, v in di.items()}
# ------------------------------------------------------------------------------------------------------------


### 두가지 기준으로 정렬
list = [[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]
list.sort(key=lambda x: (x[0], x[1]))
# 1 -1
# 1 1
# 2 2
# 3 3
# 3 4
# ------------------------------------------------------------------------------------------------------------

### 리스트안 여러 문자열 한줄 출력
words = ["a", "b", "c"]
print("\n".join(words))
# ------------------------------------------------------------------------------------------------------------

### 입력 문자의 '\n' 줄바꿈 제외하고 입력받기
import sys

sys.stdin.readline().rsplit()[0]
# or
sys.stdin.readline().strip()  # 양쪽 공백 제거
# ------------------------------------------------------------------------------------------------------------

### 해당 문자열의 숫자, 알파벳 확인
num = "1"
alpha = "abc"
print(num.isdigit())  # True
print(alpha.isalpha())  # True
# ------------------------------------------------------------------------------------------------------------


### 2차원 리스트 1차원으로 합치기
my_list = [[1, 2], [3, 4], [5, 6]]

answer = sum(my_list, [])  # [1, 2, 3, 4, 5, 6]
# ------------------------------------------------------------------------------------------------------------


### 문자열 내용 코드화하기
string = "print('abcd')"
eval(string)
# ------------------------------------------------------------------------------------------------------------


### 정규표현식 사용법
import re

string = "-10+1-20"
num = list(map(int, re.compile(r"[0-9]+").findall(string)))  # [10,1,20]
sym = re.compile(r"\+|-").findall(string)  # ["-","+","-"]
# ------------------------------------------------------------------------------------------------------------


### 2차원 리스트 90도 돌리기
# 1번 방법
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]
    # return map(list, list_of_tuples)


# 2번 방법
def rotated(a):
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


# ------------------------------------------------------------------------------------------------------------


### 몫, 나머지 동시 구하기
a, b = divmod(3, 15)
print(a, b)  # (0, 3)
# ------------------------------------------------------------------------------------------------------------


### 조합의 수 구하기 (좌표와 좌표의 최단거리 2가지 방향일때)
# nCr : n개중 r개 고르기
# 조합 공식: nCk = n! / (n-k)! x k!
from math import factorial

n, r = 9, 5  # 14개의 움직임중 오른쪽 이동 5개 고르기 (위로 4번)
print(factorial(n + r) // (factorial(n) * factorial(r)))
# ------------------------------------------------------------------------------------------------------------


### 순열의 수 구하기
# nPr : n개중 r개 나열하기
# 순열 공식: nPr =  n! / (n-r)!
from math import factorial

n, r = 9, 5  # 14개에서 5개 골라 나열하는 경우의 수
print(factorial(n + r) // factorial((n + r) - r))
# ------------------------------------------------------------------------------------------------------------


### 2차원 배열에서 일부분만 가져오기
li = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print([i[:2] for i in li])  # [[1, 2], [1, 2], [1, 2]]
# ------------------------------------------------------------------------------------------------------------


### 최소 공배수
import math

math.lcm(A, B)
# lcm = Least Common Multiple
# ------------------------------------------------------------------------------------------------------------


### Counter (카운터) 사용법
from collections import Counter

Counter("hello world")  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
Counter(["h", "e", "l", "l", "o"])  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# 개수 많은 순으로 정렬 된 배열 리턴
Counter(["h", "e", "l", "l", "o"]).most_common()  # [('l', 2), ('h', 1), ('e', 1), ('o', 1)] /

# 개수 많은 순으로 정렬 된 배열에서 n개만 리턴
Counter(["h", "e", "l", "l", "o"]).most_common(1)  # [('l', 2)]

a = Counter(["a", "a", "a", "a", "a", "b", "b", "b"])  # Counter({'a': 5, 'b': 3})
b = Counter(["b", "b", "b", "b", "b", "c", "c"])  # Counter({'b': 5, 'c': 2})
print(a, b)
# 교집합 (b는 2개다 있어서 작은값을 가져옴)
print(a & b)  # Counter({'b': 3})
# 합집합 (b는 2개다 있어서 큰값을 가져옴)
print(a | b)  # Counter({'a': 5, 'b': 5, 'c': 2})

# 덧셈 뺄셈 가능
print(a - b)  # Counter({'a': 5})
print(a + b)  # Counter({'b': 8, 'a': 5, 'c': 2})
# ------------------------------------------------------------------------------------------------------------


### 특정 기준으로 문자열 나누기
print("1 2 3".split(" "))  # ['1', '2', '3']
# ------------------------------------------------------------------------------------------------------------


### bisect(이진탐색) 사용법
from bisect import bisect_left, bisect_right

# bisect_left(literable, value) : 왼쪽 인덱스를 구하기
# bisect_right(literable, value) : 오른쪽 인덱스를 구하기
nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6]

print(bisect_left(nums1, 5))  # 5
print(bisect_right(nums1, 5))  # 6

print(bisect_left(nums2, 5))  # 1
print(bisect_right(nums2, 5))  # 9
# ------------------------------------------------------------------------------------------------------------

### 약수 빠르게 구하기
# 시간 복잡도 : O(N^(1/2))
def getDivisor(n):
    result_list = []
    for i in range(1, n ** (1 / 2) + 1):
        result_list.append(i)
        if i ** 2 == n:
            result_list.append(n // i)
    result_list.sort()
    return result_list


# ------------------------------------------------------------------------------------------------------------

### set 사용법
a = {1, 2, 3}

# 원소 추가
a.add(4)  # {1, 2, 3, 4}

# 원소 여러개 추가
a.update({5, 6})  # {1, 2, 3, 4, 5, 6}
a.update([5, 6])  # {1, 2, 3, 4, 5, 6}

# 원소 삭제 (remove는 원소 존재 안하면 에러 / discard는 에러 안남)
a.remove(6)  # {1, 2, 3, 4, 5}
a.discard(5)  # {1, 2, 3, 4}

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # 합집합 {1, 2, 3, 4, 5}
print(a & b)  # 교집합 {3}
print(a - b)  # 차집합 {1, 2}
# ------------------------------------------------------------------------------------------------------------

### 유니온 파인드
parent = list(range(vertex + 1))


def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]


# ------------------------------------------------------------------------------------------------------------

### 힙큐 사용법
import heapq as hq

heap = [6, 2, 5, 4, 1, 3]
hq.heapify(heap)  # 기존의 리스트 힙으로 만드는 함수
hq.heappush(heap, num)
n = hq.heappop(heap)

hq.heappush(heap, (-num, num))  # 최대힙처럼 사용 가능(우선 순위, 값)
# ------------------------------------------------------------------------------------------------------------