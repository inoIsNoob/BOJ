n = int(input())
a = list(map(int, input().split()))
b,c = map(int, input().split())

res = 0
for i in a:
    if i-b>0:
        if (i-b)%c == 0:
            res += (i-b)//c
        else:
            res += (i-b)//c + 1

print(res + n)
