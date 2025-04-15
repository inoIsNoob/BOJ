import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h,w,n = map(int,input().split())
    xx = (n-1)//h + 1
    yy = h if n%h == 0 else n%h
    print(str(yy)+str(xx).zfill(2))
