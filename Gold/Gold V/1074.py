def findDim(N, r, c):
    if N == 0:
        return
    
    mid = 2**(N-1)
    dim = (r >= mid) * 2 + (c >= mid)
    dimList.append(dim)
    if dim == 0:
        findDim(N-1, r, c)
    elif dim == 1:
        findDim(N-1, r, c-(2**(N-1)))
    elif dim == 2:
        findDim(N-1, r-(2**(N-1)), c)
    elif dim == 3:
        findDim(N-1, r-(2**(N-1)), c-(2**(N-1)))

dimList = []
N, c, r = map(int, input().split())
findDim(N, c, r)
result = 0

for i in range(N-1):
    result += 4**(N-1-i) * dimList[i]

print(result + dimList[-1])
