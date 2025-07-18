n = int(input())
difficult = []
for _ in range(n):
    difficult += [int(input())]

if min(difficult) == difficult[0]: print('ez')
elif max(difficult) == difficult[0]: print('hard')
else: print('?')
