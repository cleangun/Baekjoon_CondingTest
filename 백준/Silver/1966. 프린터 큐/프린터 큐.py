import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    cnt = 0
    size, target = map(int,input().split())
    sequence = deque([int(i) for i in input().rstrip().split()])
    idx_lst = deque([ int(j) for j in range(len(sequence))])
    
    while len(sequence) > 0:
        if sequence.index(max(sequence)) != 0:
            sequence.append(sequence.popleft())
            idx_lst.append(idx_lst.popleft())
        elif sequence.index(max(sequence)) == 0:
            cnt += 1
            sequence.popleft()
            if idx_lst[0] == target:
                print(cnt)
                break
            idx_lst.popleft()