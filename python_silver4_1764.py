# Baekjoon silver4 1764 듣보잡
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
namelist = set()
for _ in range(n):
  namelist.add(input().rstrip())

cnt = 0
resultlist = []
for _ in range(m):
  strr = input().rstrip()
  if strr in namelist:
    cnt += 1
    resultlist.append(strr)
print(cnt)
for arg in sorted(resultlist):
  print(arg)
