# 터렛, 마린의 위치찾기 => 두 원의 접점의 갯수 찾는 문제
import math

line = int(input())


for _ in range(line):
  x1,y1,r1, x2, y2, r2 = map(int,input().split())

  # 두 원의 중심의 거리
  dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

  
  if x1 == x2 and y1 == y2:  # 두 원의 중심이 같을 경우
    if r1 == r2:  # 두 원의 반지름 마저 같은 경우
      print(-1)
    else:  # 두 원의 반지름이 다른 경우인데, 그렇게 되면 접점이 없어짐
      print(0)
    continue
  else:    # 두 원의 중심이 다를 경우 ( 접정이 없거나, 하나 있거나, 두 개 있거나)
    if r1+r2 == dist or abs(r2-r1) == dist:
      print(1)  # 접점이 하나인 경우
    elif ((abs(r1-r2) < dist) and (dist < r1 + r2)):
      print(2)  # 접점이 두개인 경우
    else:       
      print(0)  # 접점이 없는 경우