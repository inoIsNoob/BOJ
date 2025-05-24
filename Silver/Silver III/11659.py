import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(s[i] + arr[i])

for _ in range(m):
    i, j = map(int, input().split())
    print(s[j]-s[i-1])
