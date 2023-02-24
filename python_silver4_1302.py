# python silver4 1302

import sys
import operator

input = sys.stdin.readline

N = int(input())

dic = dict()
for _ in range(N):
  data = input().rstrip()
  if data in dic:
    dic[data] = dic[data] + 1
  else:
    dic[data] = 1

# 최대값
max_value = max(dic.values())
list = []
for key, value in dic.items():
  if value == max_value:
    list.append(key)
list.sort()
print(list[0])
