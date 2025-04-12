while True:
    S = input()
    if S == '#':
        break
    print(S.count('a')+S.count('e')+S.count('i')+S.count('o')+S.count('u')+S.count('A')+S.count('E')+S.count('I')+S.count('O')+S.count('U'))
