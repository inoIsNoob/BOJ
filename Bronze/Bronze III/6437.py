st = {-2:'Double Bogey', -1:'Bogey', 0:'Par', 1:'Birdie', 2:'Eagle', 3:'Double eagle'}

cnt = 0
while True:
    p, s = map(int, input().split())
    if p == 0:
        break
    
    if s == 1:
        ans = 'Hole-in-one'
    else:
        ans = st[p-s] if p-s>=-2 else st[-2]
        
    cnt += 1
    print(f'Hole #{cnt}')
    print(ans + '.')
    print()
