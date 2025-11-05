def calFestA(x):
    winChart = {1:500, 2:300, 3:200, 4:50, 5:30, 6:10}
    if x == 0:
        return 0
    grade = 0
    for i in range(1, 7):
        grade += i
        if x <= grade:
            return winChart[i]*10000
    return 0
    
def calFestB(x):
    winChart = {1:512, 2:256, 3:128, 4:64, 5:32}
    if x == 0:
        return 0
    grade = 0
    for i in range(1, 6):
        grade += 2**(i-1)
        if x <= grade:
            return winChart[i]*10000
    return 0
        
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(calFestA(a) + calFestB(b))
