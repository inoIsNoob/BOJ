s = input()
q = []
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        q.append(s[i])    
q.append(s[-1])

print(min(q.count('0'), q.count('1')))
