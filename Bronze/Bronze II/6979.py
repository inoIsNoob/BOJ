for _ in range(int(input())):
    n = int(input())
    x = list(input().split())
    y = list(reversed(input().split()))
    big, d = 0, 0
    
    for i in range(n):
        if x[i] in y:
            d = abs(i - (n - y.index(x[i])-1))
            big = max(d, big)
            
    print(f'The maximum distance is {big}')
    print()
