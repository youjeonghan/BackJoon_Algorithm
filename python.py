"""
파이썬 알고리즘 코드
"""


### 2개의 변수에 입력을 빠르게 받아야 하는 경우
import sys

n, m = map(int, sys.stdin.readline().split())


### int형 숫자들을 빠른 속도로 입력받아 list로 만들때
import sys

li = list(map(int, sys.stdin.readline().split()))


### 조합 이용
from itertools import combinations

li = [1, 2, 3]
combi = list(combinations(li, 2))  # li 원소들의 2개를 선택한 조합의 경우가 list 안에 tuple 형식으로 저장된다.


### int의 max값 사용
import sys

int_max = sys.maxsize

### 절대값
abs_num = abs(-10)