while True:
    x, y = map(int, input().split())
    if x==y==0: break
    if x+y == 13:
        print('Never speak again.')
    else:
        if x<y:
            print('Left beehind.')
        elif x>y:
            print('To the convention.')
        else:
            print('Undecided.')
