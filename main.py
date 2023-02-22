import sys
input = sys.stdin.readline
from collections import deque

line = int(input())


for _ in range(line):
  x1,y1,r1, x2, y2, r2 = map(int,input().split())

  row= abs(x1) + abs(x2)
  column = abs(y1) + abs(y2) 
  ra = abs(r1) + abs(r2)

  # print(f"row = {row}")
  # print(f"column = {column}")
  # print(f"ra = {ra}")

  if (row + column) == ra:
    print(1)
    continue

  if ra > (row + column):
    extend = ra - max(row,column) + 1
  else:
    extend = (max((row+column) , ra) - min((row+column) , ra)) // 2
  # print(f"extend = {extend}")
  list = [ [0]*(row + 1) for i in range((column + extend))]

  

  # print(list)
  if cnt == len(list):
    cnt = -1
  print(cnt)
  # def bfs(arr):
  #   print(f"bfs")
    
    
  





         