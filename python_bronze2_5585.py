import sys

input = sys.stdin.readline

target = int(input())
remain = 1000 - target
li = [500, 100, 50, 10, 5, 1]
result = 0
print(remain)
while remain > 0:
  if li:
    if remain >= li[0]:
      remain -= li[0]
      result += 1
    else:
      li.pop(0)
  else:
    print(result)
    exit(0)
print(result)
