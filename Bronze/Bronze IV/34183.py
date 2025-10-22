n, m, a, b = map(int, input().split())
needChair = n*3
if m >= needChair:
    print(0)
else:
    print((needChair - m)*a + b)
