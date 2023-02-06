from collections import deque

# BFS 구현 -- 미완성
def BFS_mootube(graph, root, K):
  count = 0
  visited = []
  queue = deque([root])

  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.append(node)
      for index in range(len(graph[node])):
        queue += list(set(graph[node][index]) - set(visited))
        if graph[node][index][1] >= K and graph[node][index][0] not in visited:
          count += 1
  return count
    

# main 
N, Q = map(int, input().split())
graph = dict()

for i in range(1, N+1):
  graph[i] = []

for _ in range(N-1):
  a, b, usado = map(int,input().split())
  graph[a].append([b, usado])
  graph[b].append([a, usado])

print(graph)

for _ in range(Q):
  K, node = map(int, input().split())
  print(BFS_mootube(graph,node, K))




