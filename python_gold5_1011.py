import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
  li = []
  cnt = 0
  st, fi = map(int, input().split())

  plus = 1
  sep = 0
  while st < fi:
    sep += 1
    if sep % 2 == 1:  # front
      cnt += 1
      st += plus
      li.append(plus)
    else:
      cnt += 1
      st += plus
      li.append(plus)
      plus += 1
  print(cnt)
