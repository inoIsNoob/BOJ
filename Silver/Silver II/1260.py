from collections import deque

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
n,m,v = map(int ,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    n1,n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for node in graph:
    node.sort()

DFSvisited = [False] * (n+1)
BFSvisited = [False] * (n+1)

DFS(graph, v, DFSvisited)
print()
BFS(graph, v, BFSvisited)
