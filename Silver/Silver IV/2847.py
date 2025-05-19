n = int(input())
arr = list()
for _ in range(n):
    arr.append(int(input()))

result = 0
for i in range(n-1):
    if arr[-i-1] <= arr[-i-2]:
        result += arr[-i-2] - arr[-i-1] + 1
        arr[-i-2] -= arr[-i-2] - arr[-i-1] + 1
        
print(result)
