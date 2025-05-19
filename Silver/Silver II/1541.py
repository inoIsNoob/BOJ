s = input().split('-')

for j in range(len(s)):
    s[j] = s[j].split('+')
    for k in range(len(s[j])):
        s[j][k] = s[j][k].lstrip('0')
    s[j] = '+'.join(s[j])

for i in range(len(s)):
    s[i] = str(eval(s[i]))

print(eval('-'.join(s)))
