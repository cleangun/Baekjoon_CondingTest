# baekjoon silver4 2164 - 카드2
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
li = deque(list([i for i in range(1, n + 1)]))
print(li)

while len(li) > 1:
  li.popleft()
  li.append(li.popleft())
print(li[0])
