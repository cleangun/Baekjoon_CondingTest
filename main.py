import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

numList = deque(range(1,n+1))
idxList = list(map(int,input().rstrip().split()))

  
result = 0

while idxList:
  target = idxList.pop(0)
  # 발견
  if numList[0] == target:
    numList.popleft()
  else:
    where = numList.index(target)
    mid = len(numList) // 2
    if where > mid:
      while target != numList[0]:
        numList.rotate(1)
        result += 1
    else:
      while target != numList[0]:
        numList.rotate(-1)
        result += 1
    numList.popleft()
print(result)