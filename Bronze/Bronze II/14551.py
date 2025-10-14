n, m = map(int, input().split())
res= 1

for _ in range(n):
    A = int(input())
    if A:
        res *= A

print(res%m)
