from collections import deque

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
queue = deque([])
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
for i in range(h):
  for _ in range(n):
    graph[i].append(list(map(int, input().split())))

for z in range(h):
  for y in range(n):
    for x in range(m):
      if graph[z][y][x] == 1:
        queue.append((z, y, x))
        visited[z][y][x] = True

while queue:
  z, y, x = queue.popleft()
  for i in range(6):
    nz = z + dz[i]
    ny = y + dy[i]
    nx = x + dx[i]
    if 0<=nz<h and 0<=ny<n and 0<=nx<m and not visited[nz][ny][nx]:
      if graph[nz][ny][nx] == -1:
        continue
      visited[nz][ny][nx] = True
      graph[nz][ny][nx] = graph[z][y][x] + 1
      queue.append((nz, ny, nx))

def solve():
  result = 0
  for z in range(h):
    for y in range(n):
      for x in range(m):
        if graph[z][y][x] == 0:
          result = -1
          return result
        result = max(result, graph[z][y][x])
  return result-1

print(solve())
