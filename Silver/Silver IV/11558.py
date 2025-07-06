def dfs(graph, visited, start, goal):
  global cnt
  visited[start] = True

  if start == goal:
    return 0
  
  for i in graph[start]:
    if not visited[i]:
      dfs(graph, visited, i, goal)
      cnt += 1
        
for _ in range(int(input())):
  n = int(input())
    
  graph = [[] for _ in range(n + 1)]
  visited = [False for _ in range(n + 1)]
  for i in range(1, n + 1):
    graph[i].append(int(input()))

  cnt = 0
  dfs(graph, visited, 1, n)
  if not visited[n]:
    print(0)
  else:
    if n == 1:
      print(1)
    else:
      print(cnt)
