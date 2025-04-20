n=int(input())
arr=[]
PM=[]
nextNum = 1

for i in range(1,n+1):
    k = int(input())
    
    while k>=nextNum:
        arr.append(nextNum)
        nextNum += 1
        PM.append('+')
    
    if arr[-1] == k:
        arr.pop(-1)
        PM.append('-')
    else:
        print('NO')
        quit()

for i in PM:
    print(i)
