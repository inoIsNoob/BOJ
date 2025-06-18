while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    
    if (a - b)%2 == 1:
        if a - b == 1:
            pair = 0
            threePair = 0
        else:
            pair = (a - b)//2 - 1
            threePair = 1
    else:
        threePair = 0
        pair = (a - b) // 2
    
    print(pair, int(threePair))
