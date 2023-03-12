import sys
input = sys.stdin.readline

N, M = map(int,input().split())
pack = 1e9
one = 1e9
result = 0
for _ in range(M):
  six_value, one_value = map(int,input().split())
  pack = six_value if six_value < pack else pack
  one = one_value if one_value < one else one
price = {"pack" : pack, "one" : one}

def dfs(limit,cnt,sum, price, result):
  if cnt >= limit:
    if sum < result:
      return sum
    return result
  elif sum >= result:
    return result
  else:
    result = dfs(limit,cnt+6,sum+price["pack"],price,result)
    result = dfs(limit,cnt+1,sum+price["one"], price,result)
  return result

if price["pack"] >= (price["one"]*6):
  print(N * price["one"])
  exit(0)

while N >= 6:
  N -= 6
  result += price["pack"]
if N > 0:  
  result += dfs(N,0,0,price,1e9)
  print(result)
else:
  print(result)
