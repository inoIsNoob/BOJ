n = int(input())
for _ in range(n):
    v = int(input())
    number = [0] + [0 for _ in range(1000)]
    for __ in range(v):
        number[int(input())] += 1
    
    print(number.index(max(number)))
