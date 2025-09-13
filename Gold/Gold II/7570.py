n = int(input())
code = list(map(int, input().split()))
d = [0] + [0 for _ in range(n)]

for i in range(n):
    if d[code[i]-1] == 0:
        d[code[i]] = 1
    else:
        d[code[i]] = d[code[i]-1] + 1

print(n - max(d))
