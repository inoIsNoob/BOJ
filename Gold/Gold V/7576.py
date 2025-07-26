import sys
from collections import deque

def bfs(start):
  res = 0
  queue = deque([start])
  while queue:
    v = queue.popleft()
    for i in v:
      x, y = i[1], i[0]
      if x >= m or x < 0 or y >= n or y < 0:
        continue

      if not visited[y][x]:
        visited[y][x] = True
        tomato[y][x] = res
        if not queue:
            queue.append([(y+1, x), (y-1, x), (y, x+1), (y, x-1)])
        else:
            queue[0] += ((y+1, x), (y-1, x), (y, x+1), (y, x-1))
    res += 1

tomato = []
m, n = map(int, input().split())
for _ in range(n):
  tomato.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

start = []
for i in range(n):
  for j in range(m):
    if tomato[i][j] == 1:
      start.append((i, j))
    elif tomato[i][j] == -1:
      visited[i][j] = True

bfs(start)

all = True
answer = 0
for i in range(n):
  for j in range(m):
    if not visited[i][j]:
      all = False
    answer = max(answer, tomato[i][j])

if all:
  print(answer)
else:
  print(-1)
