n, k = map(int, input().split())
arr = list(map(int, input().split()))
hash = {}
start, end = 0, 0
length = 0
longer = 0
while end < n:
  hash[arr[end]] = hash.get(arr[end],0) + 1 #있으면 +=1 없으면 =1
  length += 1
  if hash.get(arr[end], 0) > k: # 마지막에 포함한게 k이상이 되어버림
    longer = max(longer, length-1)
    while hash[arr[end]] > k:
      hash[arr[start]] -= 1
      start += 1
      length -= 1
  end += 1

print(max(length, longer))
