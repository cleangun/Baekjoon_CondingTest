import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dp = deque([1,3])
for idx in range(2,n+1):
    dp.append(dp[-1]*2 + dp[-2])
    dp.popleft()
print(dp[-1]%9901)