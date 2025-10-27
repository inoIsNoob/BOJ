n, k = map(int, input().split())
pascal = [[0]] + [[1] for _ in range(n)]
if n != 1:
    pascal[2].append(1)
    for i in range(3, n+1):
        for j in range(i-2):
            pascal[i].append(pascal[i-1][j] + pascal[i-1][j+1])
        pascal[i].append(1)

print(pascal[n][k-1])
