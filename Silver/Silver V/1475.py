def ceil(n):
    if n==int(n):
        return int(n)
    return round(0.5+n)
    
n = input()
arr = [n.count(str(x)) for x in range(10)]
arr[6] += arr[9]
arr.pop(-1)
arr[6] = ceil(arr[6]/2)

print(max(arr))
