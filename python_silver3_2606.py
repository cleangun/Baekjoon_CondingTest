import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = list([set() for i in range(n)])
print(graph)

s = int(input())
for _ in range(s):
  node, con_node = map(int, input().split())
  # graph[node-1].append(con_node-1)
  # graph[con_node-1].append()
  graph[node - 1].add(con_node - 1)
  graph[con_node - 1].add(node - 1)
print(graph)


def bfs(graph):
  visited = set()
  queue = deque([0])

  while queue:
    idx = queue.popleft()
    visited.add(idx)
    for ap in graph[idx]:
      if ap not in visited:
        queue.append(ap)
  print(f"visited = {visited}")
  return len(visited) - 1


print(bfs(graph))
