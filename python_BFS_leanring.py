from collections import deque

graph_list = {1: set([3,4]),
              2: set([3,4,5]),
              3: set([1,5]),
              4: set([1]),
              5: set([2,6]),
              6: set([3,5])
             
             }
root_node = 1

print(graph_list)

def BFS_with_adj_list(graph,root):
  visited = []
  queue = deque([root])

  while queue:
    print("queue = ", queue)
    n = queue.popleft() # 왼쪽을 빼옴
    print("n = ", n)
    if n not in visited: # 방문한 적이 없으면 조건문 방문
      visited.append(n)  # 방문명록 추가
      queue += graph[n] - set(visited) # 방문한 놈들 빼고, 
                                       # 방문할 놈들 추가
      print(f"graph[{n}] = {graph[n]} , set(visited : {set(visited)})")
  return visited

print(BFS_with_adj_list(graph_list, root_node))