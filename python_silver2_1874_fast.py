# 스택 수열 - 1874 정석 ( but 시간초과 )
import sys

input = sys.stdin.readline

N = int(input())

ans = []
stack = []
i = 0

for _ in range(N):
  find_num = int(input())
  while i < find_num:
    i += 1
    stack.append(i)
    ans.append("+")
  if find_num in stack:
    while find_num != stack[-1]:
      stack.pop()
      ans.append("-")
    stack.pop()
    ans.append("-")
  else:
    print("NO")
    exit(0)
for i in ans:
  print(i)
