# 유기농 배추 - 1012 baekjoon
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


# function
def bfs(row, column, maps):
  queue = deque([])
  queue.append([row, column])
  while queue:
    x, y = queue.popleft()
    if maps[y][x] == 1:
      maps[y][x] = 0
      if x > 0:
        queue.append([x - 1, y])
      if y > 0:
        queue.append([x, y - 1])
      if x < (len(maps[0]) - 1):
        queue.append([x + 1, y])
      if y < (len(maps) - 1):
        queue.append([x, y + 1])
  return 1


for _ in range(T):
  m, n, k = map(int, input().split())
  maps = [[0] * m for i in range(n)]
  # 1의 좌표 입력받기:
  for _ in range(k):
    x, y = map(int, input().split())
    maps[y][x] = 1

  result = 0
  for y in range(len(maps)):
    for x in range(len(maps[y])):
      if maps[y][x] == 1:
        result += bfs(x, y, maps)
  print(result)
