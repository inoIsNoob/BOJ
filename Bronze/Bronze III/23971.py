h,w,n,m = map(int, input().split())

column = h//(n+1)
row = w//(m+1)

if h%(n+1) != 0 and h!=2:
    column += 1
if w%(m+1) != 0 and w!=2:
    row += 1

if column == 0:
    column = 1
if row == 0:
    row = 1

print(column * row)
