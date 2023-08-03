def solution(park, routes):
    answer = []
    graph = []
    for line in park:
        graph.append(list(line))
    for i in graph:
        print(i)
    
    visiting_node = []
    for y in range(len(graph)):
        if 'S' in graph[y]:
            visiting_node = [y, graph[y].index('S')]
            break
    print(visiting_node)
    
    for route in routes:
        direction, distance = route.split(); distance = int(distance)
        dx = 0; dy = 0
        if direction == 'E':
            dx = 1
        elif direction == 'S':
            dy = 1
        elif direction == 'W':
            dx = -1
        elif direction == 'N':
            dy = -1
        next_node = visiting_node.copy(); isOk = True
        for count in range(distance):
            next_node = [next_node[0] + dy, next_node[1] + dx]
            if (next_node[0] < 0 or next_node[0] >= len(graph)) or \
                (next_node[1] < 0 or next_node[1] >= len(graph[0])) or \
                (graph[next_node[0]][next_node[1]] == 'X'):
                isOk = False
                break
        if isOk:
            visiting_node = [next_node[0], next_node[1]]        
        print(visiting_node)
        
    answer = [visiting_node[0], visiting_node[1]]

    return answer