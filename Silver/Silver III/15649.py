import itertools

n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
nPr=itertools.permutations(arr,m)

for P in nPr:
    print(*P)
