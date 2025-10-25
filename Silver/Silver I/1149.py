import sys
input = sys.stdin.readline

n = int(input())
r, g, b = map(int, input().split())
dp = [0, 0, 0]
for _ in range(n-1):
    nr, ng, nb = map(int, input().split())
    dp[0] = nr + min(g, b)
    dp[1] = ng + min(r, b)
    dp[2] = nb + min(r, g)
    r, g, b = dp

print(min(dp))
