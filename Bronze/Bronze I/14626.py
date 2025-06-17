a = input()

s = 0
for i in range(12):
    if i % 2 == 0:
        mul = 1
    else:
        mul = 3
    if a[i] == '*':
        m = mul
        continue
    
    s += int(a[i]) * mul

for i in range(0, 10):
    if (int(a[-1]) + s + i * m)%10 == 0:
        print(i)
