k,n = map(int, input().split())
ownLAN=[int(input()) for _ in range(k)]
start, end = 1, max(ownLAN)

#이분 탐색
while start<=end:
    mid = (start+end)//2
    
    cuts = 0
    for LAN in ownLAN:
        cuts += LAN//mid
    
    if cuts >= n:
        start = mid+1
    else:
        end = mid-1

print(end)
