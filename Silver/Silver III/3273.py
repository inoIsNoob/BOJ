n = int(input())
num = list(map(int, input().split()))
x = int(input())
start, end = 0, n - 1
res = 0
num.sort()

while start < end:
    if num[start] + num[end] > x:
        end -= 1
    elif num[start] + num[end] < x:
        start += 1
    else:
        res += 1
        start += 1
        end = n - 1
    
print(res)
