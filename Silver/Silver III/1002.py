for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    r1, r2 = max(r1, r2), min(r1, r2)
  
    if r1+r2 < d or r1-r2 > d:
        ans = 0
    elif r1-r2 < d < r1+r2:
        ans = 2
    elif r1+r2 == d or r1-r2 == d:
        ans = 1
    
    if d == 0 and r1 == r2:
        ans = -1
    
    print(ans)
