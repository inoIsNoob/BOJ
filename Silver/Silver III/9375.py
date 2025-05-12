for _ in range(int(input())):
    ootd = dict()
    n = int(input())
    res = 1
    for _ in range(n):
        parts, body = input().split()
        if body not in ootd:
            ootd[body] = [parts]
        else:
            ootd[body] += [parts]
    
    for i in ootd:
        res *= len(ootd[i]) + 1
        
    print(res-1)
