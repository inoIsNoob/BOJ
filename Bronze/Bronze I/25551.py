MW, MB = map(int, input().split())
TW, TB = map(int, input().split())
PW, PB = map(int, input().split())

minW = min(MW, TB, PW)
minB = min(MB, TW, PB)

result = min(minW, minB) * 2
if minW != minB:
    result += 1

print(result)
