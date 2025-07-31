a, x, y = map(int, input().split())
r = (x**2 + y**2)**0.5

for _ in range(a):
    if int(input()) <= r:
        print('DA')
    else:
        print('NE')
