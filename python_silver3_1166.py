import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

numList = deque(range(1,n+1))
idxList = list(map(int,input().rstrip().split()))

def rt_list(temp,target,drct):
  cnt = 0
  if drct == "left":
    while temp[0] != target:
      temp.rotate(-1)
      cnt += 1
  else:
    while temp[0] != target:
      temp.rotate(1)
      cnt += 1
  return cnt
  
result = 0

while idxList:
  target = idxList.pop(0)
  # 발견
  if numList[0] == target:
    numList.popleft()
  else:
    l = rt_list(numList.copy(), target,"left")
    r = rt_list(numList.copy(), target,"right")
    
    if l > r:
      result += r
      for _ in range(r):
        numList.rotate(1)
      numList.popleft()
    else:
      result += l
      for _ in range(l):
        numList.rotate(-1)
      numList.popleft()
print(result)