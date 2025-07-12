from collections import deque

def getDistance(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] =  0
  while q:
    x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 1 and visited[nx][ny] == -1:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx,ny))
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      getDistance(i, j)
    elif graph[i][j] == 0:
      visited[i][j] = 0

for i in visited:
  print(*i)
