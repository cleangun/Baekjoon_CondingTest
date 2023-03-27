# baekjoon silver4 10845 - 큐
# 제한시간  0.5초
import sys
from collections import deque

input = sys.stdin.readline

queue = deque([])
for _ in range(int(input())):
  command = list(map(str, input().rstrip().split()))
  if len(command) > 1:  # push
    if command[0] == "push":
      queue.append(int(command[1]))
  else:
    if command[0] == "size":
      print(len(queue))
    elif command[0] == "empty":
      print(1 if len(queue) == 0 else 0)
    elif len(queue) == 0:
      print(-1)
    else:
      if command[0] == "pop":
        print(queue.popleft())
      elif command[0] == "front":
        print(queue[0])
      elif command[0] == "back":
        print(queue[-1])
