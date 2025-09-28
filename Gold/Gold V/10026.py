from collections import deque

def bfs(i, j):
    q = deque([[i, j]])
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] == arr[i][j] and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = True

def bfs2(i, j, cond):
    q = deque([[i, j]])
    while q:
        x, y = q.popleft()
        visited[x][y] = False
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]:
                if cond[0] == arr[nx][ny] or cond[1] == arr[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = False

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result1, result2 = 0, 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            result1 += 1

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            if arr[i][j] == "B":
                bfs2(i, j, "BB")
            else:
                bfs2(i, j, "RG")
            result2 += 1

print(result1, result2)
