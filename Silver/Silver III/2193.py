dp = [1, 1]
n = int(input())
for _ in range(n-2):
    dp.append(dp[-1] + dp[-2])

print(dp[-1])
