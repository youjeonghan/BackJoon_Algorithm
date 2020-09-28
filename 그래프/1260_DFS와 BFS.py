# 1260_DFS와 BFS
# 그래프

def insert_edge(graph, s, e):
    if e not in graph[s]:
        graph[s].append(e)
        graph[s].sort()

    if s not in graph[e]:
        graph[e].append(s)
        graph[e].sort()

def dfs(graph, start_node):
    visited, ready = list(), list()
    ready.append(start_node)
    while ready:
        node = ready.pop(0)
        if node not in visited:
            visited.append(node)
            for i, any_node in enumerate(graph[node]):
                ready.insert(i, any_node)
    return visited

def bfs(graph, start_node):
    visited, ready = list(), list()
    ready.append(start_node)
    while ready:
        node = ready.pop(0)
        if node not in visited:
            visited.append(node)
            ready.extend(graph[node])
    return visited

n, m, v = map(int, input().split())

# 그래프 점 찍기
graph = dict()
for i in range(n):
    graph[i+1] = list()

# 그래픈 간선 만들기
for i in range(m):
    s,e = map(int, input().split())
    insert_edge(graph, s, e)

dfs_list = dfs(graph, v)
bfs_list = bfs(graph, v)

for i in dfs_list:
    print(i, end=" ")
print()

for i in bfs_list:
    print(i, end=" ")