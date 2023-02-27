import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int,input().rstrip().split())
lis = deque([ i for i in range(1,N+1) ])

print("<",end="")
while lis:
  for _ in range(K-1):
    lis.append(lis.popleft())
  if len(lis) == 1:
    print(lis.popleft(),end="")
  else:
    print(lis.popleft(),end = ", ")

print(">")
  
