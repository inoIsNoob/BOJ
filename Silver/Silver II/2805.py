n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, int(2e9)
buff = 0
mid = (start + end)//2

while start < end + 1:
    for i in trees:
        if i > mid:
            buff += i - mid
    
    if buff >= m:
        start = mid + 1
    else:
        end = mid - 1
        
    mid = (start + end)//2
    buff = 0

print(mid)
