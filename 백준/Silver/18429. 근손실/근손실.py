import sys
input = sys.stdin.readline

n,k = map(int,input().split())
kit_lst = [int(num) for num in input().rstrip().split(" ")]    


def dfs(idx, visited, val):
    global cnt
    if val + (kit_lst[idx] - k) < 500:
        return
    
    if len(visited) == (n-1):
        cnt += 1
        return
    b = (idx,)
    new_visited = visited + b
    for index in range(n):
        if index not in list(new_visited):
            dfs(index,new_visited,val + (kit_lst[idx] - k))
    
cnt = 0
for start_idx in range(0,n):
    dfs(start_idx, (), 500)
print(cnt)