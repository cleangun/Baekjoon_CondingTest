import sys

input = sys.stdin.readline

n = int(input())
li = [3, 5]

result = -1
for sm in range(0, (n // li[0]) + 1):
  big = (n - (sm * li[0])) // li[1]
  if ((li[0] * sm) + (li[1] * big)) == n:
    result = sm + big
    break
print(result)