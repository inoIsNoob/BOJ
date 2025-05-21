def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
c = int(input())
graph = [[] for _ in range(c+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (c+1)

dfs(graph, 1, visited)
print(visited.count(True)-1)
