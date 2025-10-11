n = int(input())
arr = [int(input()) for _ in range(n)]
for i in sorted(arr, reverse=1):
    print(i)
