n = int(input())
dp = list(int(input()))
for i in range(2, n+1):
    next = list(map(int, input().split()))

    for j in range(i):
        if j == 0:
            next[j] += dp[0]
        elif j == i-1:
            next[j] += dp[-1]
        else:
            next[j] += max(dp[j-1], dp[j])
    
    dp = next

print(max(dp))
