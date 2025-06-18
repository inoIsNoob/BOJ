sec, subsec, subsubsec = 0, 0, 0
for _ in range(int(input())):
    command, word = input().split()
    if command == 'section':
        sec += 1
        secNum = str(sec)
        subsec, subsubsec = 0, 0
    elif command == 'subsection':
        subsec += 1
        secNum = str(sec) + '.' + str(subsec)
        subsubsec = 0
    elif command == 'subsubsection':
        subsubsec += 1
        secNum = str(sec) + '.' + str(subsec) + '.' + str(subsubsec)
    
    print(secNum, word)
