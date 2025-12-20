n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] + [False for _ in range(n)]
visited[1] = True

for _ in range(m):
  a,b=map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

cnt = 0
for i in graph[1]:
  if not visited[i]:
    cnt += 1
  visited[i] = True
  for j in graph[i]:
    if not visited[j]:
      cnt += 1
    visited[j] = True
    

print(cnt)
