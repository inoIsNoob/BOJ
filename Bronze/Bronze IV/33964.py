d = [0 for i in range(10)]
d[1] = 1
for i in range(2, 10):
    d[i] = d[i-1] + 10**(i-1)

x,y = map(int, input().split())
print(d[x] + d[y])
