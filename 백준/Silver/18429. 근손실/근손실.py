import sys
from collections import deque
import heapq as hq

sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

visited = [False for _ in range(n)]
ans = 0


def solve(weight):
    global n, ans, k

    if sum(visited) == n:
        ans += 1

    for i in range(n):
        if not visited[i] and weight - k + arr[i] >= 500:
            visited[i] = True
            solve(weight - k + arr[i])
            visited[i] = False

solve(500)
print(ans)
