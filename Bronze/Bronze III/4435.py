def sump(arr1, arr2):
    res = 0
    for i in range(len(arr1)):
        res += arr1[i]*arr2[i]
    return res

for i in range(int(input())):
    G = list(map(int, input().split()))
    S = list(map(int, input().split()))
    Gscore = sump(G, [1,2,3,3,4,10])
    Sscore = sump(S, [1,2,2,2,3,5,10])
    print(f'Battle {i+1}: ',end='')
    if Gscore > Sscore:
        print('Good triumphs over Evil')
    elif Gscore < Sscore:
        print('Evil eradicates all trace of Good')
    else:
        print('No victor on this battle field')
    
