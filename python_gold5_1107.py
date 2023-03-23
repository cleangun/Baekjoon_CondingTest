# baekjoon gold5 1107 - 리모컨
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
first_cnt = abs(t-100)  # + - 버튼을 이용했을 때 횟수

numlist = list([i for i in range(0,10)])
nolist = []
if n != 0:
  nolist = list(map(str,input().split()))
  for no_num in nolist:
    numlist[int(no_num)] = -1
  print(numlist)

# 예외 처리
if t == 100:
  print(0)
  exit(0)

for chidx in range(len(str(t))):
  if numlist[int(chidx)] >= 0:
    target.append(list(t)[chidx])
  else:
    target = 