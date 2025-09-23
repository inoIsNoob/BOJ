def dfs(x, y):
    global cnt
    if x<0 or y<0 or x>=m or y>=n:
        return
    if visited[y][x]:
        return
    visited[y][x] = True
    if arr[y][x] == 'P':
        cnt += 1
    if arr[y][x] == 'X':
        return
    else:
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

cnt = 0
for y in range(n):
    for x in range(m):
        if arr[y][x] == 'I':
            dfs(x, y)

print('TT' if cnt == 0 else cnt)
