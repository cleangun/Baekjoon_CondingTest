import sys

input = sys.stdin.readline

t = int(input())
btnlist = [300, 60, 10]

if (t % min(btnlist)) != 0:
  print(-1)
  exit(0)

for arg in btnlist:
  if t >= arg:
    print(t // arg, end=" ")
    t %= arg
  else:
    print(0, end=" ")
