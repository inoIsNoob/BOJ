#combination을 이용하여 간단하게 푸는 방법
import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(math.comb(b,a))

===============================================

#n!/r!*(n-r)! 으로 구현하여 푸는 방법
def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

for _ in range(int(input())):
    r,n = map(int, input().split())
    print(factorial(n)//(factorial(r)*factorial(n-r)))
