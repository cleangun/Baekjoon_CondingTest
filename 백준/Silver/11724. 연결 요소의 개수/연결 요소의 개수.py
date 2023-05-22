import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

nodes = [ [] for i in range(n+1)]

for _ in range(m):
    n1,n2 = map(int,input().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)
# main
res = 0
visited = set()
for idx in range(1,len(nodes)):
    if idx not in visited:
        res += 1
        queue = deque([idx])
        while queue:
            node_nums = queue.popleft()
            visited.add(node_nums)
            for i in nodes[node_nums]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
print(res) 