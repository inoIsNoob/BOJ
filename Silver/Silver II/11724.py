import sys
input = sys.stdin.readline

def dfs(graph, visited, i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, visited, j)
    
    return 0
        
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for k in range(1, n+1):
    if not visited[k]:
        cnt += 1
        dfs(graph, visited, k)

print(cnt)
