def change2(n):
    if n == 1 or n == 0:
        return str(n)
    return str(change2(n//2)) + str(n%2)

n = input()
if n == '0': print(0)
else:
    result = []
    for i in n:
        result.append(change2(int(i)))

    if result[0][0] == '0':
        print(result[0].lstrip('0'),end='')
    else:
        print(result[0],end='')

    for j in range(1, len(result)):
        print(result[j].zfill(3),end='')
