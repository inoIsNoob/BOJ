for _ in range(int(input())):
    a = input()
    b = input()
    
    res = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            res += 1
    
    print(f'Hamming distance is {res}.')
