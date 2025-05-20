for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    earn = 0
    
    pivot = arr[-1]
    for i in range(n-1):
        if arr[-i-2] > pivot:
            pivot = arr[-i-2]
        else:
            earn += pivot - arr[-i-2] 
    
    print(earn)
