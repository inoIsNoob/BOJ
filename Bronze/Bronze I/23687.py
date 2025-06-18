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

########################################################################################

sec = [0, 0, 0]
for _ in range(int(input())):
    command, word = input().split()
    if command == 'section':
        sec[0] += 1
        sec[1] = 0
        sec[2] = 0
    elif command == 'subsection':
        sec[1] += 1
        sec[2] = 0
    elif command == 'subsubsection':
        sec[2] += 1
    
    print('.'.join(map(str, 
    [x for x in sec if x])), word)
