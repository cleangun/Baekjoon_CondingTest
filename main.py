import sys

input = sys.stdin.readline


# function
def dfs(grd, idxy, visited):
  x, y = idxy
  if [y, x] in visited:
    return visited
  else:
    visited.append([y, x])


# main

N = int(input())

grd = [[1] * N for i in range(N)]

result = dfs(grd, [0, 0], [])

for line in grd:
  print(line)
