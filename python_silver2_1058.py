# # baekjoon 1058 - 친구
from collections import deque
n = int(input())

# function
def bfs(idx,arr):
  cnt = 0
  vindex = set()
  visited = []
  # 나랑 친구를 찾기 위한 인덱스 번호 찾기
  for chidx in range(len(arr[idx])):
    if arr[idx][chidx] == 'Y':
      vindex.add(chidx)
  print(f"first visit list = {vindex}")
  
  dist = 1
  while dist <= 2:
    indexes = set()
    for i in range(len(arr)):  # 모든 문자열을 다 돌거임
      print()
      print(f"---chekcing arr{i}---")
      haveY = []
      # 방문했거나, 기준인덱스이거나, Y가 없는경우 Pass
      if (i == idx) or ('Y' not in arr[i]) or (i in visited):
        continue
      # Y가 있는 인덱스 번호 알아내~!
      for chix in range(len(arr[i])):
        if arr[i][chix] == 'Y':
          haveY.append(chix)
      print(f"haveY = {haveY}")
      for Yidx in haveY:
        # 친구인지 확인 코드
        if Yidx in vindex:
          print("is Friend!")
          for j in haveY:
            indexes.add(j) 
          visited.append(i)
          print(f"visited change = {visited}")
          break
    vindex |= indexes
    print(f"vindex changed = {vindex}")
    dist += 1
  return cnt
        
    

# main
li = []
for _ in range(n):
  li.append(list(input()))

maxnum = 0
for idx in range(len(li)):
  if 'Y' in li[idx]:
    rt = bfs(idx,li)
    maxnum = rt if rt > maxnum else maxnum
    print(f"max = {maxnum}")
    print("------------------")
    print();print()
  
  else:
    continue
print(maxnum)
    

