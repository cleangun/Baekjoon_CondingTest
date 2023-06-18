import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())

graph = [ [] for i in range(n+1)]
# 입력
for _ in range(n-1):
    node1, node2, distance = map(int,input().rstrip().split())
    graph[node1].append((node2,distance))
    graph[node2].append((node1,distance))
    
def find_node(Snode, Fnode):
    visited = set()
    visited.add(Snode)
    queue = deque(graph[Snode])
    while queue:
        idx,distance = queue.popleft()
        visited.add(idx)
        if idx == Fnode:
            return distance
        else:
            for element in graph[idx]:
                if element[0] not in visited:
                    queue.append((element[0], element[1]+distance))
                
    
# 결과 출력
for _ in range(m):
    Snode, Fnode = map(int,input().rstrip().split())
    print(find_node(Snode,Fnode))