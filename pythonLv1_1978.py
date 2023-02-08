input()
arr = list(map(int,input().split()))
result = 0

for i in range(len(arr)):
  if arr[i] == (1 or 0):
    continue
  cnt = 1
  
  for j in range(2,arr[i]+1):
    if arr[i] % j == 0:
      cnt += 1
  if cnt <= 2:
    result += 1

print(result)