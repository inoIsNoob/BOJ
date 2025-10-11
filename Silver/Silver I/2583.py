from collections import deque

m, n, k = map(int, input().split())
visited = [[False for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(m-y2, m-y1):
        for x in range(x1, x2):
            visited[y][x] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
empty = 0
result2 = list()
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[y][x] = True
            empty += 1
            area = 0
            q = deque([(i, j)])
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0<=ny<m and 0<=nx<n and not visited[ny][nx]:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        area += 1
            result2.append(area)

print(empty)
for item in sorted(result2):
    if not item:
        print(1,end=' ')
    else:
        print(item,end=' ')
