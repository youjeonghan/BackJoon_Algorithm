# 골드 1레벨
# 다시 풀기

n, k = map(int, input().split())
li = list(map(int, input().split()))

answer = 0
socket = set()
for idx in range(len(li)):
    if len(socket) < n:
        socket.add(li[idx])
    elif li[idx] not in socket:
        flag = False
        for i in range(idx + 1, len(li)):
            if li[i] in socket:
                socket.discard(li[i])
                flag = True
        if flag == False:
            socket.pop()
        answer += 1
        socket.add(li[idx])
print(answer)