# 미로만들기 하기 싫다;;; 1374
import sys
from collections import deque

input = sys.stdin.readline
maps = deque(["."])

N = int(input())
movelist = input().rstrip()
print(movelist)
# movelist = movelist.split("F")
# print(movelist)

direction = "down"
for od in movelist:
  if od == "F":
    if direction == "down":
      print("down")
