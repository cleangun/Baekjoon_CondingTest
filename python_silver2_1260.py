# baekjoon silver2 1260 - dfs와bfs
import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for i in range(n + 1)]
for _ in range(m):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)


def dfs(graph, node, visited):
  if node not in visited:
    print(node, end=" ")
    visited.append(node)
    for arg in sorted(graph[node]):
      if arg not in visited:
        visited = dfs(graph, arg, visited)
  return visited


def bfs(graph, queue):
  visited = []
  while queue:
    node = queue.popleft()
    if node not in visited:
      print(node, end=" ")
      visited.append(node)
      for i in sorted(graph[node]):
        if i not in visited:
          queue.append(i)


dfs(graph, v, [])
print()
bfs(graph, deque([v]))
