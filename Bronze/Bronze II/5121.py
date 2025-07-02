for _ in range(int(input())):
    n, w = map(int, input().split())
    data = list(map(int, input().split()))
    movingAv = list()
    for i in range(n - w + 1):
        movingAv.append(sum(data[i:i+w]) // w)
    
    print(f'Data Set {_+1}:')
    print(max(movingAv) - min(movingAv))
    print()
