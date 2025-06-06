a = sorted(list(input()))
b = sorted(list(input()))
apb = list()
same = 0

for i in a:
    if i not in apb:
        apb.append(i)
        if i in b:
            same += 2*min(a.count(i), b.count(i))
        
print(len(a)+len(b)-same)
