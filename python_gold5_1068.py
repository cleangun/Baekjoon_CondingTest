import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = list([set() for i in range(n)])

idx = 0
for value in list(map(int, input().split())):
  if value != -1:
    graph[value].add(idx)
  idx += 1
print(graph)

rid_node = int(input())
cnt = 0
visited = []

# rid node process
queue = deque([rid_node])

while queue:
  idx = queue.popleft()
  print(f"deleting idx {idx}")
  visited.append(idx)

  for j in graph[idx]:
    if j not in visited:
      queue.append(j)

print(f"deleted nodes = {visited}")

for i in range(len(graph)):
  if i not in visited:
    queue.append(i)
    print(f"visiting node = {i}")
    while queue:
      idx = queue.popleft()
      visited.append(idx)
      if len(graph[idx]) == 0 or ((len(graph[idx]) <= 1) and (rid_node in graph[idx])):
        cnt += 1
        continue
      
      for j in graph[idx]:
        if j not in visited:
          queue.append(j)
print(cnt)