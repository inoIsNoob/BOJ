def capitalize(word):
    return word[0].upper() + word[1:]
  
n, v = input().split(); n = int(n)
if n == 1:
    print(v)
    for i in v:
        if i.isupper():
            print('_' + i.lower(), end='')
        else:
            print(i, end='')
    print()
    print(v[0].upper() + v[1:])

elif n == 2:
    w = v.split('_')
    print(w[0],end=''.join([capitalize(w[i]) for i in range(1, len(w))]))
    print()
    print(v)
    print(''.join([capitalize(w[i]) for i in range(len(w))]))

elif n == 3:
    print(v[0].lower() + v[1:])
    print(v[0].lower(), end='')
    for i in range(1, len(v)):
        if v[i].isupper():
            print('_' + v[i].lower(), end='')
        else:
            print(v[i], end='')
    print()
    print(v)
