while True:
    res = 0
    a=int(input())
    if a == 0:
        break
    for i in range(a+1):
        res = res+i
    print(res)
