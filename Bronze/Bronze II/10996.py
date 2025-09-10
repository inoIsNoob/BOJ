a = int(input())

col1 = ("* ") * ((a-1)//2 + 1)
col2 = (" *") * ((a-1)//2)
if a%2 == 1:
    for i in range(2*a):
        if i%2 == 0:
            print(col1)
        else:
            if a != 1:
                print(col2)
else:
    for i in range(2*a):
        if i%2 == 0:
            print(col1)
        else:
            print(" " + col1)
