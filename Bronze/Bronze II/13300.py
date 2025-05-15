def ceil(n):
    if n==int(n):
        return int(n)
    return round(0.5+n)
    
n,k = map(int, input().split())
arr = [[0,0] for _ in range(7) ]
for _ in range(n):
    s,y = map(int, input().split())
    arr[y][s] += 1

res = 0
for i in range(1, 7):
    for j in range(2):
        res += ceil(arr[i][j]/k)

print(res)
