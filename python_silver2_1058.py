# # baekjoon 1058 - 친구
from collections import deque
n = int(input())

# function
def bfs(idx,arr):
  cnt = 0
  tovisit = deque([idx])
  visited = [idx]
  
  for _ in range(2):
    indexes = []
    while tovisit:
      a = tovisit.popleft()
      for i in range(len(arr)):  # 모든 문자열을 다 돌거임
        # 방문했거나, 기준인덱스이거나, Y가 없는경우 Pass
        if (i == idx) or ('Y' not in arr[i]) or (i in visited):
          continue
        # 친구인지 확인
        if arr[a][i] == 'Y':
          visited.append(i)
          indexes.append(i)
          cnt += 1
    for list_to_visit in indexes:
      tovisit.append(list_to_visit)
  return cnt
  
# main
li = []
for _ in range(n):
  li.append(list(input()))

maxnum = 0
for idx in range(len(li)):
  if 'Y' in li[idx]:
    n1 = bfs(idx,li)
    if n1 > maxnum:
        maxnum = n1
print(maxnum)