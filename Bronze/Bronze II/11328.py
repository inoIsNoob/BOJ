for _ in range(int(input())):
    s1, s2 = input().split()
    s1, s2 = list(s1), list(s2)
    s1.sort(); s2.sort()
    if s1==s2: print('Possible')
    else : print('Impossible')
