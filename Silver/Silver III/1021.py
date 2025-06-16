n, m = map(int, input().split())
loc = list(map(int, input().split()))
queue = [x for x in range(1, n+1)]

res = 0
while loc:
    right = queue[:queue.index(loc[0])]
    left = queue[queue.index(loc[0]):]
    res += min(len(left), len(right))
    
    queue = left[1:]+right
    loc.pop(0)

print(res)
