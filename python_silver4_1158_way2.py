import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
lis = deque([i for i in range(1, N + 1)])
result = []
while lis:
  for _ in range(K - 1):
    lis.rotate(-1)
  result.append(str(lis.popleft()))

print("<" + ", ".join(result) + ">")
