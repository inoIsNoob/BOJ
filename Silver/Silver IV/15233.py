a,b,g = map(int, input().split())
teamA = list(input().split())
teamB = list(input().split())
scoreA, scoreB = 0, 0
for player in list(input().split()):
    if player in teamA:
        scoreA += 1
    else:
        scoreB += 1
    
if scoreA > scoreB:
    print('A')
elif scoreA < scoreB:
    print("B")
else:
    print("TIE")
