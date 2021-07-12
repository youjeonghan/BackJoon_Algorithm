from sys import stdin

read = stdin.readline


start, target = map(int,read().split())

result =0
def bfs(num, cnt):
    global result
    if result or num>target:
        return
    if num == target:
        result = cnt +1
    
    else:
        bfs(int(str(num)+"1"), cnt+1)
        bfs(num*2, cnt+1)

bfs(start, 0)
print(result if result else -1)