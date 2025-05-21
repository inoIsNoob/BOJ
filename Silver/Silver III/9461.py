d = [0] * 101
d[1],d[2],d[3] = 1,1,1
d[4],d[5] = 2,2

for _ in range(int(input())):
    n = int(input())
    for i in range(6, n+1):
        if d[i] == 0:
            d[i] = d[i - 1] + d[i - 5]

    print(d[n])
