from collections import deque
def solution(n, computers):
    answer = 0
    visited = set()
    
    for i in range(n):
        if i not in visited:
            queue = deque([i])
            while queue:
                node = queue.popleft()
                visited.add(node)
                for linked_node_idx in range(len(computers[i])):
                    if (linked_node_idx == i) or (linked_node_idx in visited):
                        continue
                    if computers[node][linked_node_idx] == 1:
                        queue.append(linked_node_idx)
            answer += 1
    
    return answer