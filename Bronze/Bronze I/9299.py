def isOneDiff(w1, w2):
    diff = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
    if diff == 1: return True
    else: return False

while True:
    w = input()
    if w == '#': break
    else:
        flag = True
        while True:
            nw = input()
            if nw == '#':
                break
            
            if flag:
                if len(w) == len(nw) and isOneDiff(w, nw):
                    flag = True
                    w = nw
                else:
                    flag = False

        if flag:
            print('Correct')
        else:
            print("Incorrect")
