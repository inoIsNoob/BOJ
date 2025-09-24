n = int(input())
d = [0, 1]

for i in range(2, n+1):
    if i**0.5 == int(i**0.5):
        d.append(1)
    else:
        minValue = 4
        for j in range(1, int(i**0.5)+1):
            minValue = min(minValue, d[j*j] + d[i - j*j])
        d.append(minValue)

print(d[-1])
