# 골드 5레벨        N-Queen
# 다시
N = int(input())
li = [0] * N
c = []
m = []
p = []
for i in range(N):  # i행
    result = []
    for j in range(N):  # j열
        if j not in c:
            pass