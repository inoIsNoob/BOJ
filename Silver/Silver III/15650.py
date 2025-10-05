import itertools

n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
nPr=itertools.permutations(arr,m)

for P in nPr:
    for i in range(m-1):
        if P[i] >= P[i+1]:
            break
    else:
        print(*P)
