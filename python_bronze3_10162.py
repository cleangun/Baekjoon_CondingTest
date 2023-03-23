import sys

input = sys.stdin.readline

t = int(input())
btnlist = [300, 60, 10]

if (t % 10) == 0:
  for arg in btnlist:
    print(t // arg, end=" ")
    t %= arg
else:
  print(-1)
