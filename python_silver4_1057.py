# 토너먼트 하면서 두 수가 만나는 라운드 찾는 문제
# => dfs로 해결 (원리만 안다면 불필요) -> 문제 그대로 해당 두 선수가 있으면
# 무조건 이기는 식으로 다음 라운드 dfs로 넘김, 
# 두 선수가 한 번에 잡히면 return 해서 나옴

import sys
input = sys.stdin.readline
from collections import deque

N, p1, p2 = map(int,input().split())

list = deque([])
for i in range(1,N+1):
  list.append(i)



def chk(chk_target, p1 , p2):
  if chk_target == p1:
    return p1
  elif chk_target == p2:
    return p2
  else:
    return 0


def dfs(lis,p1,p2,cnt):
  cnt += 1
  list = deque([])
  while len(lis) > 0:
    if len(lis) >= 2:
      pn1 = lis.popleft()
      pn2 = lis.popleft()

      if pn1 in (p1,p2) or pn2 in (p1,p2):  # 임환수 김지민 있음
        if pn1 in (p1,p2) and pn2 in (p1,p2):  # 임환수 김지민 둘 다 만남
          print(cnt)
          exit(0)
        else:
          list.append(max(chk(pn1,p1,p2), chk(pn2,p1,p2)))
      else:   # 임화수와 김지민이 없음
        list.append(pn2)
        
    else:  # 홀수 인 경우
      list.append(lis.pop())
  dfs(list,p1,p2,cnt)
  

dfs(list,p1,p2,0)
          
        
  

  