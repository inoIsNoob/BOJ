n = int(input())
m = int(input())
S = list(input())
cnt = 0
result = 0
i = 0

while i < m-2:
    if S[i] == "I":
        start = i
        while i < m-2:
            if S[i+1] == "O":
                if S[i+2] == "I":
                    cnt += 2
                    i += 2
                else:
                    i += 1
                    break
            else:
                i += 1
                break
        length = i - start + 1
        if (length+1)//2 - n > 0:
            result += (length+1)//2 - n
    else:
        i += 1
    
print(result)
