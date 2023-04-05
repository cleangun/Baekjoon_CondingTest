# baekjoon silver1 - 2178 - 미로탐색
# dfs로 했을 때 RecursionError가 발생해서 실패했으나
# bfs로 아이디어가 떠올라서 적용하니 정답
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list([int(digit) for digit in input().rstrip()]))


def find_route(graph, queue, level):
  ix = [1, 0, -1, 0]
  iy = [0, 1, 0, -1]
  result = 0

  while level <= (n * m):
    level += 1
    tmp = []
    while queue:
      x, y = queue.popleft()
      if (x == (m - 1)) and (y == (n - 1)):
        return level

      for i in range(4):
        dx = x + ix[i]
        dy = y + iy[i]
        if (dx >= 0) and (dx < m) and (dy >= 0) and (dy < n):
          if graph[dy][dx] == 1:
            graph[dy][dx] = 0
            tmp.append([dx, dy])
    for arg in tmp:
      queue.append(arg)
    # print(f"queue = {queue}")
  return -1


graph[0][0] = 0
queue = deque([[0, 0]])
print(find_route(graph, queue, 0))