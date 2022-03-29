# 골드 5레벨
# 다시 풀기
from collections import deque

s = int(input())

deq = deque([(0, 1, 0)])  # 시간, 현재 개수, 복사한 수

while deq:
    t, cnt, copy_cnt = deq.popleft()
    if cnt == s:
        print(t)
        break

    if cnt != copy_cnt:
        deq.append((t + 1, cnt, cnt))
    if cnt - 1 >= 2:
        deq.append((t + 1, cnt - 1, copy_cnt))
    if cnt + copy_cnt <= 1000:
        deq.append((t + 1, cnt + copy_cnt, copy_cnt))
