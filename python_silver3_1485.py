# 정사각형 문제
import sys
import math
input = sys.stdin.readline
sqrt = math.sqrt
pow = math.pow

# function
def get_distance(ax1,ax2):
  return ((ax1[0] - ax2[0]) ** 2 + (ax1[1] - ax2[1]) ** 2 ) ** (1/2)

# main
N = int(input())
for _ in range(N):
  axisList = []
  for _ in range(4):
    axisList.append(list(map(int,input().split())))
  
  dist = []
  for i in range(3):
    for j in range(i+1,4):
      dist.append(get_distance(axisList[i] , axisList[j]))

  dist.sort()

  if (dist[0] == dist[1]) and (dist[1] == dist[2]) and (dist[2] == dist[3]):
    if dist[4] == dist[5]:
      print(1)
      continue
    else:
      print(0)
      continue
  else:
    print(0)
    continue